from .models import Post
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q #Multiple filter conditions
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets, status
from rest_framework.response import Response

from comments.models import Comment  
from likes.models import Like 
from .serializers import PostSerializer 
from comments.serializers import CommentSerializer  
from likes.serializers import *  


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        self.perform_create(serializer)  # Call the default perform_create method
        return Response({'status': status.HTTP_201_CREATED, 'payload': serializer.data, 'message': 'Post created successfully', 'user': user.username})
    
        """
        if serializer.validated_data['creator'] != user:
             return Response({'status': status.HTTP_403_FORBIDDEN, 'tried in the name of': serializer.data["creator"], 'message': 'You can only create posts for yourself', 'user': user.username })
        else:
            self.perform_create(serializer)  # Call the default perform_create method
            return Response({'status': status.HTTP_201_CREATED, 'payload': serializer.data, 'message': 'Post created successfully', 'user': user.username })
        """
        
    def post_by_content_or_title(self, request, str):
        queryset = self.get_queryset()
        if str:
            queryset = queryset.filter(
                Q(title__icontains=str) | Q(content__icontains=str)
            )

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class AdvancedPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    
    def get_advanced_view(self, request, pk=None):
        try:
            post = self.get_object()
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        comments = Comment.objects.filter(post=post)
        comments_data = CommentSerializer(comments, many=True).data

        post_data = PostSerializer(post).data

        response_data = {
            'post': post_data,
            'comments': comments_data
        }

        return Response(response_data)