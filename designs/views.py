from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .models import Design, Comment
from .serializers import DesignSerializer, CommentSerializer

class DesignListView(ListCreateAPIView):
    ''' List View for /designs INDEX/LIST CREATE '''
    queryset = Design.objects.all()
    serializer_class = DesignSerializer

class DesignDetailView(RetrieveUpdateDestroyAPIView):
    ''' Detail View for /designs/id SHOW UPDATE DELETE '''
    queryset = Design.objects.all()
    serializer_class = DesignSerializer

#url => /designs/designId/comments POST

class CommentListView(APIView):
    ''' List View for /designs/designId/comments CREATE comments'''

    def post(self, request, design_pk):
        request.data['design'] = design_pk
        created_comment = CommentSerializer(data=request.data)
        if created_comment.is_valid():
            created_comment.save()
            return Response(created_comment.data, status=status.HTTP_201_CREATED)
        return Response(created_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


# url /designs/designId/comments/commentId DELETE

class CommentDetailView(APIView):
    '''Delete Comment View'''

    def delete(self, _request, **kwargs):

        comment_pk = kwargs['comment_pk']
        try:
            comment_to_delete = Comment.objects.get(pk=comment_pk)
            comment_to_delete.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            raise NotFound(detail='Comment Not Found')

