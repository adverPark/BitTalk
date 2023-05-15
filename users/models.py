from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class GenderChoice(models.TextChoices):
        MALE = ("male", "남")
        FEMALE = ("female", "여")

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )

    last_name = models.CharField(
        max_length=150,
        editable=False,
    )

    name = models.CharField(
        max_length=150,
        default="",
    )

    premium_user = models.BooleanField(
        default=False,
    )
    avatar = models.URLField(blank=True)

    gender = models.CharField(
        max_length=10,
        choices=GenderChoice.choices,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "회원"
