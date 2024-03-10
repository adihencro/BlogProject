from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'updated', 'timestamp', 'creator']


class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'updated', 'timestamp', 'creator')

        def create(self, validated_data):
            post = Post
            post.title = validated_data['title']
            post.content = validated_data['content']
            post.timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
            post.updated = models.DateTimeField(auto_now=True, auto_now_add=False)
            post.creator = models.ForeignKey(User, on_delete=models.CASCADE)
            post.save()
            return post()


    """
        def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        post.save()  
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)  # Update fields if present
        instance.content = validated_data.get('content', instance.content)

        # Update timestamps automatically or as needed (adjust logic)
        instance.updated = models.DateTimeField(auto_now=True)  # Auto-update on save

        instance.save()
        return instance
    """

    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name', 'email', 'bio']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username', 'email', 'password', 'first_name', 'last_name', 'bio')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.bio = validated_data['bio']
        user.save()
        return user
    