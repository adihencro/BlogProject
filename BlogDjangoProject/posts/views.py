#from django.shortcuts import render
#from django.shortcuts import HttpResponse
from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q #Multiple filter conditions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


"""
def home_page(request):
    return HttpResponse("Hello!! It's my API blog project.")
"""

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow only authenticated users to create/update

    @action(detail=False, methods=['get'])
    def post_by_content_or_title(self, request, str):
        queryset = self.get_queryset()
        if str:
            queryset = queryset.filter(
                Q(title__icontains=str) | Q(content__icontains=str)
            )

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
       

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(detail=False, methods=['get'])
    def user_by_name(self, request, name):
      queryset = self.get_queryset()
      if name:
          queryset = queryset.filter(
              Q(first_name__icontains=name) | Q(last_name__icontains=name)
          )

      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data)
    
    