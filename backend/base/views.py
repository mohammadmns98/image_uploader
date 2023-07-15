from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import ImageModel
from .serializers import ImageSerializer


class ImageList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    model = ImageModel
    serializer_class = ImageSerializer
    queryset = ImageModel.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class UserImageList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        userImages = ImageModel.objects.filter(
            user__username=request.user.username)
        serializer = ImageSerializer(userImages, many=True)
        return Response(serializer.data)


class ImageRetrieve(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'id'

# class DeleteImage(generics.DestroyAPIView):
#     serializer_class = ImageSerializer
#     queryset = ImageModel.objects.all()
