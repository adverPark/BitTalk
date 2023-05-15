from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.PostApiView.as_view()),
    path("<int:pk>", views.PostDetailApiView.as_view()),
    path("<int:pk>/comment", views.PostCommentAPIView.as_view()),
    path("<int:pk>/photo", views.PostPhotos.as_view()),
    re_path(
        r"(?P<slug>[\w\u3131-\u3163\uac00-\ud7a3-]+)/$",
        views.PostDetailBySlugApiView.as_view(),
    ),
    path(
        "category/",
        views.CategoryViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "category/<int:pk>/",
        views.CategoryViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path("comment/", views.CommentAPIView.as_view()),
    path("comment/<int:pk>", views.CommentDetailAPIView.as_view()),
]
