from django.test import TestCase
from django.test import Client
from Homepage.models import *

class TestLoginView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.user = User.objects.create(
            first_name='Incybro',
            last_name='Sho',
            email='incybro@gmail.com',
            username='Incybro',
            is_superuser=True
        )
        cls.password = 'secret'
        cls.user.set_password(cls.password)
        cls.user.save()
    def test_user_login(self):
        login = self.client.login(username=self.user.username, password=self.password)
        self.assertTrue(login)
