from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q #Multiple filter conditions
from rest_framework.permissions import *
from rest_framework.authtoken.models import Token
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]


    @action(detail=False, methods=['get'])
    def user_by_name(self, request, name):
      queryset = self.get_queryset()
      if name:
          queryset = queryset.filter(
              Q(first_name__icontains=name) | Q(last_name__icontains=name)
          )

      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data)
    
"""
class RegisterUser(APIView):
   def post(self, request):
      serializer = UserSerializer(data=request.data)

      if not serializer.is_valid():
         return Response({'status' : 403, 'errors': serializer.errors, 'message': 'something wrong'})
      
      serializer.save()

      user = User.objects.get(username = serializer.data['username'])
      token_obj ,_ = Token.objects.get_or_create(user=user)

      return Response({'status' : 200, 'payload' : serializer.data, 'token' : str(token_obj), 'message' : 'Success'})
"""


class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # Allow anyone to register

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user = User.objects.get(username = serializer.data['username'])
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'status': status.HTTP_201_CREATED,
            'payload': serializer.data,
            'token': str(token),
            'message': 'User registered successfully'
        })

    

    

    
    