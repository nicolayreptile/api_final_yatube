from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.serializers import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

from .models import Post, Comment, Group, Follow


User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('created', )


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, required=False)
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('pub_date', )


class GroupSerializer(serializers.ModelSerializer):

    posts = PostSerializer(many=True, required=False)

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username', default=CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        read_only=False, slug_field='username', 
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ['user', 'following']
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following']
            )
        ]