from django.urls import path, include
from .views import *
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)
router.register(r'user/register', UserRegistrationViewSet)
router.register(r'post/add', AddPostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/user/name/<str:name>/', UserViewSet.as_view({'get': 'user_by_name'})),
    path('api/post/include/<str:str>/', PostViewSet.as_view({'get': 'post_by_content_or_title'})),
    path("", views.home_page, name="HOME"),
]