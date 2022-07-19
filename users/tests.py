from django.test import TestCase
from users.models import Diet, Meals, MealHistory, Preferences
from django.contrib.auth.models import User
# from django.utils import unittest


class UserTestCase(TestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user(
            'Ali', 'ali@live.com', 'password')

    def test_user(self):
        self.assertEqual(self.user_1.email, 'ali@live.com')


class DietTestCase(TestCase):
    def setUp(self):
        self.diet = Diet.objects.create(
            vegan=False, vegetarian=False, gluten_free=False, ketogenic=False, pescetarian=False, paleo=True)

    def test_diet(self):
        self.assertEqual(self.diet.paleo, True)
        self.assertEqual(self.diet.vegan, False)
        self.assertEqual(self.diet.vegetarian, False)
        self.assertEqual(self.diet.ketogenic, False)
        self.assertEqual(self.diet.pescetarian, False)


class MealsTestCase(TestCase):
    def setUp(self):
        self.meal = Meals.objects.create(
            breakfast=True, lunch=False, dinner=False, dessert=False, snack=False)

    def test_diet(self):
        self.assertEqual(self.meal.breakfast, True)
        self.assertEqual(self.meal.lunch, False)
        self.assertEqual(self.meal.dinner, False)
        self.assertEqual(self.meal.dessert, False)
        self.assertEqual(self.meal.snack, False)


class MealHistoryTestCase(TestCase):
    def setUp(self):
        self.meal = MealHistory.objects.create(
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


class PreferencesTestCase(TestCase):
    def setUp(self):
        self.preferences = Preferences.objects.create(
            calories_limit=0, intolorences=['dairy', 'egg', 'wheat'], budget=5)

    def test_diet(self):
        self.assertEqual(self.preferences.calories_limit, 0)
        self.assertEqual(self.preferences.intolorences,
                         ['dairy', 'egg', 'wheat'])
        self.assertEqual(self.preferences.budget, 5)
