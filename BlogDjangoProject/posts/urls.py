from django.urls import path, include
from .views import *
from rest_framework import routers
from django.urls import re_path


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
#router.register(r'post/add', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/posts/include/<str:str>/', PostViewSet.as_view({'get': 'post_by_content_or_title'})),
    path('api/posts/create/', PostViewSet.as_view({'post': 'post'})),
]

