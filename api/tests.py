from rest_framework.test import APITestCase, APIClient
from django.test import TestCase

from django.contrib.auth.models import User
from .models import Post


class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='123456789')
        Post.objects.create(
            title='test title', content='test content', author=self.user)

    def test_post_created(self):
        count = Post.objects.all().count()
        post = Post.objects.get(id=1)

        self.assertEqual(count, 1)
        self.assertEqual(post.title, 'test title')
        self.assertEqual(post.content, 'test content')
        self.assertEqual(post.author, self.user)


class PostViewAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='123456789')
        Post.objects.create(
            title='test title', content='test content', author=self.user)
        self.client.force_authenticate(user=self.user)

    def test_post_list(self):
        response = self.client.get('/api/posts/')
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, [{"id": 1, "title": "test title", "content": "test content", "author": "testuser"}])
    
    def test_post_detail(self):
        response = self.client.get('/api/posts/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"id": 1, "title": "test title", "content": "test content", "author": "testuser"})
