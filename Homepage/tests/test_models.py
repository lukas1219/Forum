from django.test import TestCase
from django.test import Client
from Homepage.models import *

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create(username="Test")
        cls.user.save()
        cls.category = Category.objects.create(title="Testowa")
        cls.category.save()
        username = cls.user.username
        Post.objects.create(title="Post title", description="Some content here", author=cls.user, category=cls.category)
    def test_post_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertTrue(field_label,'title')
    def test_post_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)
    def test_category_title_label(self):
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('title').verbose_name
        self.assertTrue(field_label,'title')
    def test_category_title_max_length(self):
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)
