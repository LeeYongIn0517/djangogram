from django.urls import reverse
from django.test import TestCase

class TestPosts(TestCase):

    def test_get_posts_page(self):
        url = reverse('posts:posts_create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/posts_create.html')