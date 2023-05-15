from django.db import models
from common.models import CommonModel


class Photo(CommonModel):
    file = models.URLField()
    description = models.CharField(
        max_length=140,
        null=True,
        blank=True,
    )

    blog = models.ForeignKey(
        "blog.Post",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="photos",
    )

    def __str__(self) -> str:
        return "Potho File"


class Video(CommonModel):
    file = models.URLField()

    blog = models.ForeignKey(
        "blog.Post",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="videoes",
    )

    def __str__(self) -> str:
        return "Vidio File"
