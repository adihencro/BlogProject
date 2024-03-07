#from django.shortcuts import render
#from django.shortcuts import HttpResponse
from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework import viewsets


def home_page(request):
    return HttpResponse("Hello!! It's my API blog project.")

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class UserRegistrationViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserRegistrationSerializer

     

        