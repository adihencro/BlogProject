from rest_framework import serializers
from .models import User
from rest_framework.authtoken.models import Token
    

class UserSerializer(serializers.ModelSerializer):
    #password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'bio'] 


