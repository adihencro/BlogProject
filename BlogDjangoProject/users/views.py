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
from django.shortcuts import get_object_or_404



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
        #token, _ = self.token_model.objects.create(user=user)
        token, created = Token.objects.get_or_create(user=user)   
        return Response({
            'status': status.HTTP_200_OK,
            'payload': serializer.data,
            'token': str(token),
            'message': 'User logged successfully'
        })
    
"""
class LoginUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginUserSerializer
    permission_classes = [AllowAny] 

    def login(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, username=serializer.data['username'])
        if not user.check_password(serializer.data['password']):
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)

        #tempUsers = TempUserForAuth.objects.all()
        #for user in tempUsers:
         #   user.delete()

        return Response({
            'status': status.HTTP_200_OK,
            'payload': serializer.data,
            'token': str(token),
            'message': 'User logged successfully'
        })

class LoginUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  

    def login(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            'status': status.HTTP_200_OK,
            'payload': serializer.data,
            'token': str(token),
            'message': 'User logged successfully'
        })

class LoginView(APIView):
    def get_in(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            #auth_data = get_tokens_for_user(request.user)
            token, created = Token.objects.get_or_create(user=user)     
            return Response({'msg': 'Login Success', **token}, status=status.HTTP_200_OK)
        
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

"""

      


