from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Design, Comment
from .serializers import DesignSerializer, CommentSerializer, PopulatedDesignSerializer, NewDesignSerializer

class DesignListView(ListCreateAPIView):
    ''' List View for /designs INDEX/LIST CREATE '''
    # queryset = Design.objects.all()
    # serializer_class = DesignSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    def post(self, request):
        request.data['added_by'] = request.user.id
        serialized_design = NewDesignSerializer(data=request.data)
        if serialized_design.is_valid():
            serialized_design.save()
            print(serialized_design.data)
            return Response(serialized_design.data)
        return Response(serialized_design.errors)

    def get(self, request):
        designs = Design.objects.all()
        serialized_designs = DesignSerializer(designs, many=True)
        return Response(serialized_designs.data)

class DesignDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /designs/id SHOW UPDATE DELETE '''
    queryset = Design.objects.all()
    serializer_class = DesignSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

#url => /designs/designId/comments POST

class CommentListView(APIView):
    ''' List View for /designs/designId/comments CREATE comments'''

    permission_classes = (IsAuthenticated, )

    def post(self, request, design_pk):
        request.data['design'] = design_pk
        request.data['owner'] = request.user.id
        request.data['added_by'] = request.user.id
        created_comment = CommentSerializer(data=request.data)
        if created_comment.is_valid():
            created_comment.save()
            return Response(created_comment.data, status=status.HTTP_201_CREATED)
        return Response(created_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


# url /designs/designId/comments/commentId DELETE

class CommentDetailView(APIView):
    '''Delete Comment View'''

    permission_classes = (IsAuthenticated, )

    def delete(self, _request, **kwargs):

        comment_pk = kwargs['comment_pk']
        try:
            comment_to_delete = Comment.objects.get(pk=comment_pk)
            comment_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise NotFound(detail='Comment Not Found')

class DesignSaveView(APIView):
    '''Add saved to a design or remove if already saved'''

    permission_classes = (IsAuthenticated, )

    def post(self, request, design_pk):
        try:
            design_to_save = Design.objects.get(pk=design_pk)
        except Design.DoesNotExist:
            raise NotFound()
        
        if request.user in design_to_save.saved_by.all():
            design_to_save.saved_by.remove(request.user.id)
        else:
            design_to_save.saved_by.add(request.user.id)
        
        serialized_design = DesignSerializer(design_to_save)

        return Response(serialized_design.data, status=status.HTTP_202_ACCEPTED)