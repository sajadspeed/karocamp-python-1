from django.db.models import Prefetch
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import CustomUser
from .models import Post, Tag, Like, Comment
from .serializers import (
    PostListSerializer,
    PostDetailSerializer,
    PostCreateSerializer,
    CommentSerializer,
)


# --- LIST VIEWS ---
class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = Post.objects.select_related('author').prefetch_related('tags', 'likes', 'comments')
        sort = self.request.query_params.get('sort', 'desc')
        return qs.order_by('created_at') if sort == 'asc' else qs.order_by('-created_at')


class PostListByTagView(PostListView):
    def get_queryset(self):
        tag = get_object_or_404(Tag, name=self.kwargs['tag_name'])
        return super().get_queryset().filter(tags=tag)


class PostListByAuthorView(PostListView):
    def get_queryset(self):
        author = get_object_or_404(CustomUser, username=self.kwargs['username'])
        return super().get_queryset().filter(author=author)


# --- DETAIL VIEW ---
class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        ordered_comments = Comment.objects.select_related('author').order_by('-created_at')
        return Post.objects.select_related('author').prefetch_related(
            'tags',
            'likes__user',
            Prefetch('comments', queryset=ordered_comments),
        )


# --- CREATE VIEWS (Protected by JWT Authentication) ---
class PostCreateView(generics.CreateAPIView):
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Assign the authenticated user as the post author
        serializer.save(author=self.request.user)


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        serializer.save(post=post, author=self.request.user)


# --- ACTION VIEW ---
class PostLikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            # Toggle: remove like if it already exists
            like.delete()

        return Response(
            {
                'liked': created,
                'like_count': post.like_count,
            },
            status=status.HTTP_200_OK,
        )
