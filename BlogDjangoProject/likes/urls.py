from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('likes/post/create', LikePostViewSet.as_view({'post': 'create'})),
    path('likes/comment/create', LikeCommentViewSet.as_view({'post': 'create'}))
]

