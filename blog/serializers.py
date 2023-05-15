from rest_framework import serializers
from .models import Category, Comment, Post
from users.serializers import TinyUserSeriallizer
from medias.serializer import PhotoSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = (
        #     "pk",
        #     "name",
        # )
        exclude = (
            "created_at",
            "updated_at",
        )


class CommentSerializer(serializers.ModelSerializer):
    author = TinyUserSeriallizer(read_only=True)

    class Meta:
        model = Comment
        fields = (
            "author",
            "text",
        )


class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "pk",
            "title",
            "content",
            "category",
            "photos",
        )


class PostDetailSerializer(serializers.ModelSerializer):
    author = TinyUserSeriallizer(read_only=True)
    category = CategorySerializer(read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)
    # comments = CommentSerializer(
    #     many=True,
    #     read_only=True,
    # )

    class Meta:
        model = Post
        fields = "__all__"
