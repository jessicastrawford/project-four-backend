from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Design, Comment

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'profile_image')

class NestedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'profile_image')

class NestedDesignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Design
        fields = ('name', 'added_by')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class PopulatedCommentSerializer(CommentSerializer):
    owner = NestedUserSerializer()

class PopulatedDesignSerializer(NestedDesignSerializer):
    added_by = NestedUserSerializer()

class DesignSerializer(serializers.ModelSerializer):
    comments = PopulatedCommentSerializer(many=True, read_only=True)
    saved_by = NestedUserSerializer(many=True, read_only=True)
    added_by = UserSerializer()

    class Meta:
        model = Design
        fields = '__all__'

class NewDesignSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Design
        fields = '__all__'
