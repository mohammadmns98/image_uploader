from rest_framework import serializers
from .models import CustomUser
# from base.serializers import ImageSerializer
# from base.models import ImageModel


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id','username','email','password']
        extra_kwargs={
            'password':{'write-only':True},
        }

    def create(self, validated_data):
        print("=====================================")
        print(validated_data)
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

