from rest_framework import serializers
from .models import Like


class LikePostSerializer(serializers.ModelSerializer):
    liked_by_username = serializers.ReadOnlyField(source='liked_by.username')  

    class Meta:
        model = Like
        fields = ['id', 'timestamp', 'liked_by', 'liked_by_username', 'post_id'] 
        
class LikeCommentSerializer(serializers.ModelSerializer):
    liked_by_username = serializers.ReadOnlyField(source='liked_by.username')  

    class Meta:
        model = Like
        fields = ['id', 'timestamp', 'liked_by', 'liked_by_username', 'comment_id'] 