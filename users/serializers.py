from rest_framework.serializers import ModelSerializer
from .models import User


class TinyUserSeriallizer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "username",
            "avatar",
        )


class PrivateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )
