from django.urls import path
from .views import PostListAPIView, PostDetailAPIView


urlpatterns = [
    path('posts/', PostListAPIView.as_view()),
    path('posts/<int:pk>/', PostDetailAPIView.as_view()),
]