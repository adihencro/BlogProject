from rest_framework import serializers
from .models import User
from rest_framework.exceptions import APIException
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.db.models.signals import pre_save
    

class UserSerializer(serializers.ModelSerializer):
    #password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'bio'] 

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.email = validated_data['email']
        user.bio = validated_data['bio']
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        fields = ('username', 'password')
        extra_kwargs = {
            'username': {'description': 'The username of the user.'},
            'password': {'description': 'The password of the user.'},
        }
        title = 'Login Serializer'
        description = 'Serializer for user login.'

    def validate(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise APIException(detail="Invalid username or password.", status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            raise APIException(detail="Invalid username or password.", status=status.HTTP_401_UNAUTHORIZED)

        return user

"""
class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password'] 

        def login(self, validated_data):
            user = User
            user.username=validated_data['username']
            user.set_password(validated_data['password'])
            pre_save(user)
"""


