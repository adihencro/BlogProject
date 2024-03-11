from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/users/name/<str:name>/', UserViewSet.as_view({'get': 'user_by_name'})),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/users/register', RegisterUserViewSet.as_view({'post' : 'create'})),
]

