from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from django.db import IntegrityError
from posts.serializers import PostSerializer
from comments.serializers import CommentSerializer
from posts.models import Post
from comments.models import Comment 
from .models import Like
from .serializers import *



class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikePostSerializer
    permission_classes = [IsAuthenticated]

    
class LikePostViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikePostSerializer
    permission_classes = [IsAuthenticated]  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_id = request.data['post_id']            
        
        if post_id:
            try:
                like = serializer.save()
                post = Post.objects.get(pk=post_id)
                post_data = PostSerializer(post, many=False).data
                post.likes.add(like)
                return Response({'status': status.HTTP_201_CREATED, 'payload' : serializer.data, 'post' : post_data})  
            except IntegrityError as e:
                return Response('You can only like a post or comment once.')
        
        
        return Response({'status': status.HTTP_200_OK, 'message': "'post_id' is invalid"})

class LikeCommentViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeCommentSerializer
    permission_classes = [IsAuthenticated]  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        comment_id = request.data['comment_id']

        if comment_id:
            like = serializer.save()
            comment = Comment.objects.get(pk=comment_id)
            comment_data = CommentSerializer(comment, many=False).data
            comment.likes.add(like) 
            return Response({'status': status.HTTP_201_CREATED, 'payload' : serializer.data, 'comment' :  comment_data})
        
        return Response({'status': status.HTTP_200_OK, 'message': "'comment_id' is invalid"})



  

        