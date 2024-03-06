#from django.shortcuts import render
#from django.shortcuts import HttpResponse
from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Hello!! It's my API blog project.")

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
