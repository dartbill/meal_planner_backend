from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from jsonfield import JSONField
from datetime import date


# Create your models here.


class Diet(models.Model):
    # default value of boolean is None unless setting default attribute
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    ketogenic = models.BooleanField(default=False)
    pescetarian = models.BooleanField(default=False)
    paleo = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.username


class Meals(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    dessert = models.BooleanField(default=False)
    snack = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id.username


class MealHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.CharField(max_length=50)
    recipes = JSONField(models.CharField(max_length=512))

    def __str__(self):
        return self.user_id.username


class Preferences(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    diet_id = models.ForeignKey(
        Diet, on_delete=models.SET_NULL, blank=True, null=True)
    meals_id = models.ForeignKey(
        Meals, on_delete=models.SET_NULL, blank=True, null=True)
    calories_limit = models.CharField(max_length=500)
    intolorences = JSONField(models.CharField(
        max_length=100))  # make this an array
    budget = models.CharField(max_length=500)

    def __str__(self):
        return self.user_id.username
