from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework.authtoken.views import ObtainAuthToken
from .views import LoginView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('users/name/<str:name>/', UserViewSet.as_view({'get': 'user_by_name'})),
    path('users/api-token-auth/', views.obtain_auth_token),
    path('users/register', RegisterUserViewSet.as_view({'post' : 'create'})),
    path('users/login/', LoginView.as_view()),
    path('users/get_advanced_view/<int:pk>', AdvancedUserViewSet.as_view({'get' : 'get_advanced_view'}))
    #path('api/users/login', LoginView.as_view({'post': 'get_in'}), name='login'),
]

