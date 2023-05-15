from django.contrib import admin
from .models import Category, Post, Comment
import re


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "category",
        "is_published",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "author",
        "is_published",
        "category",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
