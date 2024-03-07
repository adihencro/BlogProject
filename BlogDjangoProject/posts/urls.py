from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'user/register', UserRegistrationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("", views.home_page, name="HOME")
]