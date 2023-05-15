from django.contrib import admin
from .models import Chat_room, Message


@admin.register(Chat_room)
class Chat_roomAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "created_at",
        "updated_at",
    )


@admin.register(Message)
class MessgeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "text",
        "created_at",
    )
