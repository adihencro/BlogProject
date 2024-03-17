from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/posts/include/<str:str>/', PostViewSet.as_view({'get': 'post_by_content_or_title'})),
    path('api/posts/create/', PostViewSet.as_view({'post': 'post'})),
    path('api/posts_advanced/<int:pk>}', AdvancedPostViewSet.as_view({'get' : 'get_advanced_view'}))
]

