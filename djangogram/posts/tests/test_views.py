from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase


class TestPosts(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username = 'yongin', email = 'yongin@gmail.com', password ='secret'
        )

    def test_get_posts_page(self):
        url = reverse('posts:posts_create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/posts_create.html')

    def test_post_creating_posts(self):
        login = self.client.login(username = "yongin", email = "yongin@gmail.com", password = "secret")
        self.assertTrue(login)

        url = reverse('posts:posts_create')
        image = SimpleUploadedFile("test.jpeg", b"This is a palace")
        response = self.client.post(
            url,
            {'image': image, 'caption':'test test'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/base.html")

    def test_post_creating_posts_not_login(self):
        url = reverse('posts:posts_create')
        image = SimpleUploadedFile("test.jpeg", b"This is a palace")
        response = self.client.post(
            url,
            {'image': image, 'caption':'test test'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/main.html")
