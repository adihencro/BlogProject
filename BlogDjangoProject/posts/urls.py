from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/include/<str:str>/', PostViewSet.as_view({'get': 'post_by_content_or_title'})),
    path('posts/create/', PostViewSet.as_view({'post': 'post'})),
    path('posts/advanced_view/<int:pk>}', AdvancedPostViewSet.as_view({'get' : 'get_advanced_view'}))
]

