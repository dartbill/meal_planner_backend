from django.test import TestCase, Client, RequestFactory
from users.models import Diet, Meals, MealHistory, Preferences
from django.contrib.auth.models import User
from .views import new_user
from django.urls import reverse
import pytest
import json
# from django.utils import unittest


class UserTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user(
            'Ali', 'ali@live.com', 'password')

    def test_user(self):
        self.assertEqual(self.user_1.email, 'ali@live.com')


class DietTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.diet = Diet.objects.create(user_id=self.user,
                                        vegan=False, vegetarian=False, gluten_free=False, ketogenic=False, pescetarian=False, paleo=True)

    def test_diet(self):
        self.assertEqual(self.diet.paleo, True)
        self.assertEqual(self.diet.vegan, False)
        self.assertEqual(self.diet.vegetarian, False)
        self.assertEqual(self.diet.ketogenic, False)
        self.assertEqual(self.diet.pescetarian, False)
        self.assertEqual(self.diet.__str__(), 'testuser')


class MealsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.meal = Meals.objects.create(user_id=self.user,
                                         breakfast=True, lunch=False, dinner=False, dessert=False, snack=False)

    def test_diet(self):
        self.assertEqual(self.meal.breakfast, True)
        self.assertEqual(self.meal.lunch, False)
        self.assertEqual(self.meal.dinner, False)
        self.assertEqual(self.meal.dessert, False)
        self.assertEqual(self.meal.snack, False)
        self.assertEqual(self.meal.__str__(), 'testuser')


class MealHistoryTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.meal = MealHistory.objects.create(user_id=self.user,
                                               today_date='19/07/22', recipes={
                                                   "breakfast": [{"id": "", "title": "", "fave": ""}],
                                                   "lunch": [{"id": "", "title": "", "fave": ""}],
                                                   "dinner": [{"id": "", "title": "", "fave": ""}],
                                                   "dessert": [{"id": "", "title": "", "fave": ""}],
                                                   "snacks": [{"id": "", "title": "", "fave": ""}]})

    def test_diet(self):
        self.assertEqual(self.meal.today_date, '19/07/22')
        self.assertEqual(self.meal.recipes, {
            "breakfast": [{"id": "", "title": "", "fave": ""}],
            "lunch": [{"id": "", "title": "", "fave": ""}],
            "dinner": [{"id": "", "title": "", "fave": ""}],
            "dessert": [{"id": "", "title": "", "fave": ""}],
            "snacks": [{"id": "", "title": "", "fave": ""}]})
        self.assertEqual(self.meal.__str__(), 'testuser')


class PreferencesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.preferences = Preferences.objects.create(user_id=self.user,
                                                      calories_limit=0, intolorences=['dairy', 'egg', 'wheat'], budget=5)

    def test_diet(self):
        self.assertEqual(self.preferences.calories_limit, 0)
        self.assertEqual(self.preferences.intolorences,
                         ['dairy', 'egg', 'wheat'])
        self.assertEqual(self.preferences.budget, 5)
        self.assertEqual(self.preferences.__str__(), 'testuser')


class TestRoutes(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_user_creation_route(self):

        data = {"name": 'name', 'email': 'email@email.com',
                'password': 'password'}
        json_data = json.dumps(data)
        response = self.client.post(
            '/createuser/', content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, 200)

    def test_login_route(self):
        self.user = User.objects.create_user(
            username='testuser', email='email@email.com', password='password')
        data = {"email": "email@email.com", "password": "password"}
        json_data = json.dumps(data)
        response = self.client.post(
            '/login/', content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, 200)

    def test_login_route_no_user(self):
        self.user = User.objects.create_user(
            username='testuser', email='email@email.com', password='password')
        data = {"email": "email@email.com", "password": "hello"}
        json_data = json.dumps(data)
        response = self.client.post(
            '/login/', content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_email(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        data = {"message": "hi this is from the web!",
                "html": "<h1>test html</h1>"}
        json_data = json.dumps(data)
        response = self.client.post(
            '/email/', content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, 200)

    def test_post_meal_history(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        data = {
            "today_date": "18/07/2022",
            "recipes": {
                "breakfast": [{"id": "", "title": "", "fave": ""}],
                "lunch": [{"id": "", "title": "", "fave": ""}],
                "dinner": [{"id": "", "title": "", "fave": ""}],
                "dessert": [{"id": "", "title": "", "fave": ""}],
                "snacks": [{"id": "", "title": "", "fave": ""}]}}
        json_data = json.dumps(data)
        response = self.client.post(
            '/mealhistory/', content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, 200)

    def test_get_meal_history(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        response = self.client.get(
            '/mealhistory/')
        self.assertEqual(response.status_code, 200)

    def test_patch_prefs(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        data = {
            "prefs": {"calories_limit": {"breakfast": 2, "lunch": 2, "dinner": 2, "snack": 2, "dessert": 2},
                      "intolorences": ["dairy", "egg"],
                      "budget": {"breakfast": 2, "lunch": 2, "dinner": 2, "snack": 2, "dessert": 2}},
            "diet": {"vegan": True, "vegetarian": True, "glutenfree": True, "ketogenic": True, "pescetarian": True, "paleo": True},
            "meals": {"breakfast": True, "lunch": True, "dinner": True, "dessert": True, "snack": True}
        }
        json_data = json.dumps(data)
        response = self.client.patch(
            '/prefs/', content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, 200)

    def test_post_prefs(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        data = {
            "prefs": {"calories_limit": {"breakfast": 2, "lunch": 2, "dinner": 2, "snack": 2, "dessert": 2},
                      "intolorences": ["dairy", "egg"],
                      "budget": {"breakfast": 2, "lunch": 2, "dinner": 2, "snack": 2, "dessert": 2}},
            "diet": {"vegan": True, "vegetarian": True, "glutenfree": True, "ketogenic": True, "pescetarian": True, "paleo": True},
            "meals": {"breakfast": True, "lunch": True, "dinner": True, "dessert": True, "snack": True}
        }
        json_data = json.dumps(data)
        response = self.client.post(
            '/createprefs/', content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, 200)

    def test_get_prefs(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

        response = self.client.get(
            '/prefs/')
        self.assertEqual(response.status_code, 200)

    def test_post_prefs_notauthenticated(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        # self.client.login(username='testuser', password='12345')
        data = {
            "prefs": {"calories_limit": {"breakfast": 2, "lunch": 2, "dinner": 2, "snack": 2, "dessert": 2},
                      "intolorences": ["dairy", "egg"],
                      "budget": {"breakfast": 2, "lunch": 2, "dinner": 2, "snack": 2, "dessert": 2}},
            "diet": {"vegan": True, "vegetarian": True, "glutenfree": True, "ketogenic": True, "pescetarian": True, "paleo": True},
            "meals": {"breakfast": True, "lunch": True, "dinner": True, "dessert": True, "snack": True}
        }
        json_data = json.dumps(data)
        response = self.client.post(
            '/createprefs/', content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, 200)

    def test_patch_prefs__notauthenticated(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        # self.client.login(username='testuser', password='12345')
        data = {
            "prefs": {"calories_limit": {"breakfast": 2, "lunch": 2, "dinner": 2, "snack": 2, "dessert": 2},
                      "intolorences": ["dairy", "egg"],
                      "budget": {"breakfast": 2, "lunch": 2, "dinner": 2, "snack": 2, "dessert": 2}},
            "diet": {"vegan": True, "vegetarian": True, "glutenfree": True, "ketogenic": True, "pescetarian": True, "paleo": True},
            "meals": {"breakfast": True, "lunch": True, "dinner": True, "dessert": True, "snack": True}
        }
        json_data = json.dumps(data)
        response = self.client.patch(
            '/prefs/', content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, 200)

    def test_get_meal_history_notauthenticated(self):
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        # self.client.login(username='testuser', password='12345')

        response = self.client.get(
            '/mealhistory/')
        self.assertEqual(response.status_code, 200)
