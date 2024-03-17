from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'updated', 'timestamp', 'creator']

class AdvancedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id']  
    
