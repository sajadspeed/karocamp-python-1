from rest_framework import serializers
from .models import Post, Tag, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at']
        read_only_fields = ['id', 'author', 'created_at']


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    content_preview = serializers.SerializerMethodField()
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    like_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'content_preview', 'tags', 'like_count', 'comments_count', 'created_at']

    def get_content_preview(self, obj):
        # Truncate post content to first 20 words for timeline preview
        words = obj.content.split()
        if len(words) > 20:
            return ' '.join(words[:20]) + ' ...'
        return obj.content

    def get_like_count(self, obj):
        return len(obj.likes.all())

    def get_comments_count(self, obj):
        return len(obj.comments.all())


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    like_count = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()
    liked_by = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'content',
            'tags',
            'like_count',
            'user_has_liked',
            'liked_by',
            'comments',
            'created_at',
        ]

    def get_like_count(self, obj):
        return len(obj.likes.all())

    def get_user_has_liked(self, obj):
        # Check whether the authenticated user has liked this post
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return any(like.user_id == request.user.id for like in obj.likes.all())
        return False

    def get_liked_by(self, obj):
        # Return usernames of all users who liked this post
        return [like.user.username for like in obj.likes.all()]


class PostCreateSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.CharField(max_length=50),
        required=False,
        write_only=True,
    )

    class Meta:
        model = Post
        fields = ['id', 'content', 'tags', 'created_at']
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        tag_names = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)

        # Create or fetch tags and attach them to the post
        for name in tag_names:
            cleaned_name = name.strip()
            if cleaned_name:
                tag, _ = Tag.objects.get_or_create(name=cleaned_name)
                post.tags.add(tag)

        return post

    def to_representation(self, instance):
        # Return full post details after creation
        return PostDetailSerializer(instance, context=self.context).data
