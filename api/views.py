from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend

from api import serializers
from api.models import Post, Group, Follow
from api.permissions import IsOwnerOrReadOnly


User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Post.objects.all()
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('group', )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Group.objects.all()


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FollowSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Follow.objects.all()
    filter_backends = (filters.SearchFilter, )
    search_fields = ('=user__username', '=following__username')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)