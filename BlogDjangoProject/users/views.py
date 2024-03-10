from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q #Multiple filter conditions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


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
    
    