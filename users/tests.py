from django.test import TestCase
from users.models import Diet, User
from django.contrib.auth.models import User
# from django.utils import unittest

class DietTestCase(TestCase):
    def setUp(self):
        Diet.objects.create(vegan=False, vegetarian=False, gluten_free = False, ketogenic =False,pescetarian = False, peleo = True )
        # User.objects.create_user(username="Ali")
        self.user_1 = User.objects.create_user('Ali', 'ali@live.com', 'password')
       

    def test_user(self):
        self.assertEqual(self.user_1.email, 'ali@live.com')
