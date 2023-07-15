from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import CustomUser
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class CreateUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveUser(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
