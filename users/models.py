from django.db import models
from django.contrib.auth.models import User
# from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Diet(models.Model):
    # default value of boolean is None unless setting default attribute
    vegan = models.BooleanField()
    vegetarian = models.BooleanField()
    gluten_free = models.BooleanField()
    ketogenic = models.BooleanField()
    pescetarian = models.BooleanField()
    peleo = models.BooleanField()

    def __str__(self):
        return self.preferences_id


class Meals(models.Model):
    breakfast = models.BooleanField()
    lunch = models.BooleanField()
    dinner = models.BooleanField()
    dessert = models.BooleanField()
    snack = models.BooleanField()

    def __str__(self):
        return self.preferences_id


class MealHistory(models.Model):
    User_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    breakfast = models.BooleanField()
    # recipes = models.ArrayField(
    #     models.CharField(max_length=512)
    # )

    def __str__(self):
        return self.preferences_id


class Preferences(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    diet_id = models.ForeignKey(Diet, on_delete=models.SET_NULL, null=True)
    meals_id = models.ForeignKey(Meals, on_delete=models.SET_NULL, null=True)
    calories_limit = models.IntegerField()
    intolorences = models.CharField(max_length=50)
    budget = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.user_id
