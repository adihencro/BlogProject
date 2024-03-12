from .models import User
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q #Multiple filter conditions
from rest_framework.permissions import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    #set the authentication scheme 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


    @action(detail=False, methods=['get'])
    def user_by_name(self, request, name):
      queryset = self.get_queryset()
      if name:
          queryset = queryset.filter(
              Q(first_name__icontains=name) | Q(last_name__icontains=name)
          )

      serializer = self.serializer_class(queryset, many=True)
      return Response(serializer.data)
    

class RegisterUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]  

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


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        #if not user.is_active:
        #    return Response({'error': 'User is inactive'}, status=403)
        
        #token, _ = self.token_model.objects.create(user=user)
        token, created = Token.objects.get_or_create(user=user)   
        response_data = {'status': status.HTTP_201_CREATED, 'token': token.key, 'username': user.username, 'message': 'User logged successfully'}  
        return Response(response_data)
