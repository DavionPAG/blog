from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

 
# Create your tests here.


class PostsTests(TestCase):
  def setUp(self):
     self.user = get_user_model().objects.create_user(
       'Tester',
       'tester@test.io'
     )

     Post.objects.create(
       title = ' Words',
       author = self.user,
       body = 'TEST',
     )

  def test_post_list_status_code(self):
       response = self.client.get('/blog/')
       self.assertEqual(response.status_code, 200)

  def test_post_detail_status_code(self):
       response = self.client.get('/blog/posts/1/')
       self.assertEqual(response.status_code, 200)

  def test_post_create_status_code(self):
       response = self.client.get('/blog/posts/new/')
       self.assertEqual(response.status_code, 302)

  def test_post_delete_status_code(self):
       response = self.client.get('/blog/posts/1/delete/')
       self.assertEqual(response.status_code, 302)

  def test_post_edit_status_code(self):
       response = self.client.get('/blog/posts/1/edit/')
       self.assertEqual(response.status_code, 302)