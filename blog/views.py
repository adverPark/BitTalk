from .models import Category, Comment, Post
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    PostListSerializer,
    PostDetailSerializer,
)
from medias.serializer import PhotoSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.conf import settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostDetailBySlugApiView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def get_object(self):
        queryset = self.get_queryset()
        filter_kwargs = {"slug": self.kwargs["slug"]}
        return get_object_or_404(queryset, **filter_kwargs)


class PostApiView(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        post = Post.objects.all()
        serializer = PostListSerializer(
            post,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = PostDetailSerializer(
                data=request.data,
            )
            if serializer.is_valid():
                category_pk = request.data.get("category")
                new_post = serializer.save(
                    author=request.user,
                )
                print(dir(new_post))
                if not category_pk == None:
                    try:
                        add_category = Category.objects.get(pk=category_pk)
                    except Category.DoesNotExist:
                        raise ParseError("카테고리가 존재하지 않습니다.")

                    new_post.category = add_category
                    new_post.save()

                return Response(PostListSerializer(new_post).data)
            else:
                return Response(serializer.errors)
        else:
            raise NotAuthenticated


class PostDetailApiView(APIView):
    def object_get(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        post = self.object_get(pk)
        return Response(PostDetailSerializer(post).data)

    def put(self, request, pk):
        post = self.object_get(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if not request.user.is_superuser or not request.user.is_staff:
            raise PermissionDenied
        serializer = PostDetailSerializer(
            post,
            request.data,
            partial=True,
        )
        if serializer.is_valid():
            if "category" in request.data:
                category_pk = request.data.get("category")

                if category_pk is not None:
                    try:
                        chage_category = Category.objects.get(pk=category_pk)
                    except Category.DoesNotExist:
                        raise ParseError("카테고리가 존재하지 않습니다.")

                    post.category = chage_category

                else:
                    post.category = None

            updated_post = serializer.save()
            return Response(
                PostDetailSerializer(updated_post).data,
            )
        else:
            Response(serializer.errors)

    def delete(self, request, pk):
        post = self.object_get(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if not request.user.is_superuser or not request.user.is_staff:
            raise PermissionDenied
        post.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CommentAPIView(APIView):
    def get(self, request):
        all_comment = Comment.objects.all()
        serializer = CommentSerializer(
            all_comment,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(
            data=request.data,
        )
        if serializer.is_valid():
            new_comment = serializer.save()
            return Response(CommentSerializer(new_comment).data)
        else:
            return Response(serializer.errors)


class CommentDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        return Response(
            CommentSerializer(
                self.get_object(pk),
            ).data
        )

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(
            comment,
            request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_comment = serializer.save()
            return Response(
                CommentSerializer(updated_comment).data,
            )
        else:
            Response(serializer.errors)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class PostCommentAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        try:
            page = request.query_params.get("page", 1)
            page = int(page)
        except ValueError:
            page = 1
        page_size = settings.PAGE_SIZE
        start = page - 1
        end = start + page_size
        post = self.get_object(pk)
        serializer = CommentSerializer(
            post.comments.all()[start:end],
            many=True,
        )
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            new_comment = serializer.save(
                author=request.user,
                post=self.get_object(pk),
            )
            serializer = CommentSerializer(new_comment)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PostPhotos(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound

    # def get(self, request, pk):
    #     pass

    def post(self, request, pk):
        blog = self.get_object(pk)
        if not request.user.is_authenticated:
            raise NotAuthenticated
        if not request.user.is_superuser or not request.user.is_staff:
            raise PermissionDenied
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            photo = serializer.save(
                blog=blog,
            )
            serializer = PhotoSerializer(photo)
            return Response(serializer.data)

        else:
            return Response(serializer.errors)

    # def delete(self, request, pk):
    #     pass
