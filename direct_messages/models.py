from django.db import models
from common.models import CommonModel


class Chat_room(CommonModel):
    participants = models.ManyToManyField(
        "users.User",
    )

    def __str__(self) -> str:
        return "Chatting Room"


class Message(CommonModel):
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="messages",
    )
    chat_room = models.ForeignKey(
        "direct_messages.Chat_room",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self) -> str:
        return f"{self.user} : {self.text}"
