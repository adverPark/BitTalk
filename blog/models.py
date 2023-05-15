from django.db import models
from common.models import CommonModel
import re


def custom_slugify(value):
    # 공백을 '-'로 대체
    value = re.sub(r"\s+", "-", value)
    # 연속되는 '-' 제거
    value = re.sub(r"\-{2,}", "-", value)
    # 양 끝의 '-' 제거
    value = value.strip("-")
    # 특수 문자 삭제
    value = re.sub(r"[^\w\s-]", "", value)
    return value


class Category(CommonModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "카테고리"


class Post(CommonModel):
    title = models.CharField(max_length=200)

    content = models.TextField()

    author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="posts",
    )

    category = models.ForeignKey(
        "blog.Category",
        on_delete=models.ManyToManyField,
        null=True,
        blank=True,
        related_name="posts",
    )

    # image = models.ImageField(
    #     upload_to="blog_images/",
    #     null=True,
    #     blank=True,
    # )

    slug = models.SlugField(
        unique=True,
        max_length=255,
        blank=True,
    )

    is_published = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "포스트"

    def save(self, *args, **kwargs):
        if not self.slug or (
            not self.pk and Post.objects.filter(slug=self.slug).exists()
        ):
            self.slug = custom_slugify(self.title)
            # 겹치는 슬러그가 있을 경우 unique한 슬러그 생성
            unique_slug = self.slug
            num = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{self.slug}-{num}"
                num += 1
            self.slug = unique_slug

        super(Post, self).save(*args, **kwargs)


class Comment(CommonModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = "댓글"
