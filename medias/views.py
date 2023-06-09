from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Photo
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class PhotoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound

    def delete(self, request, pk):
        photo = self.get_object(pk)
        # print(dir(photo))
        if photo.blog.author != request.user:
            raise PermissionDenied
        photo.delete()
        return Response(status=HTTP_200_OK)
