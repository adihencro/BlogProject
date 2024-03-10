#from django.shortcuts import render
#from django.shortcuts import HttpResponse
from .models import *
from .serializers import *
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q #Multiple filter conditions



def home_page(request):
    return HttpResponse("Hello!! It's my API blog project.")

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer

  @action(detail=False, methods=['get'])
  def post_by_content_or_title(self, request, str):
      queryset = self.get_queryset()
      if str:
          queryset = queryset.filter(
              Q(title__icontains=str) | Q(content__icontains=str)
          )

      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data)

class AddPostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = AddPostSerializer

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

class UserRegistrationViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserRegistrationSerializer

"""
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = AddPostSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been used, we need to invalidate the
            # prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
"""
