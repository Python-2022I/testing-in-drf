from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Post
from django.contrib.auth.models import User

from .serializers import PostSerializer, UserSerializer


class PostListAPIView(APIView):
    def get(self, request: Request) -> Response:
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailAPIView(APIView):
    def get(self, request: Request, pk: int) -> Response:
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
