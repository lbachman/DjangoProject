from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from people.views import UserViewSet, PostViewSet, CommentViewSet, LikeViewSet

# Define router for API endpoints
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', include(router.urls)),   # Include API endpoints from router
    # You can include additional URLs for your app here if needed
]

# Remove the duplicated code block
