from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
    

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


