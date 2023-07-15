from rest_framework import serializers
from users.models import CustomUser
from .models import ImageModel
from users.serializers import UserSerializer


class ImageSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField(source="user.email")
    user = UserSerializer(many=False,read_only=True)

    # user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = ImageModel
        # fields = ['id','image','created_at','user']
        fields = '__all__'
