from django.test import TestCase
from Homepage.models import *
from django.test import Client
from django.urls import reverse

class PostListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create(username="Test")
        cls.user.save()
        cls.category = Category.objects.create(title="Testowa")
        cls.category.save()
        number_od_posts = 7

        for post_pk in range(number_od_posts):
            Post.objects.create(
                author=cls.user,
                title=f'Title {post_pk}',
                description=f'Description {post_pk}',
                category=cls.category,
            )
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_view_url_is_accessible_by_name(self):
            response = self.client.get(reverse('posts_list'))
            self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Homepage/posts_list.html')
