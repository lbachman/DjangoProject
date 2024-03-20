from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PostViewSet, CommentViewSet, LikeViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import authenticate
from .views import signup
from django.urls import path



router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),  # Add this line for login
    path('signup/', signup, name='signup'),
]
