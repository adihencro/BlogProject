from django.urls import path, include
from .views import PostViewSet
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("", views.home_page, name="HOME")
]