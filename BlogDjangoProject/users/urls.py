from django.urls import path, include
from .views import UserViewSet
from rest_framework import routers
from django.urls import re_path


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
#router.register(r'post/add', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/users/name/<str:name>/', UserViewSet.as_view({'get': 'user_by_name'})),
]

