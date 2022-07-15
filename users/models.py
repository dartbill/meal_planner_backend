from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Diet(models.Model):
    # default value of boolean is None unless setting default attribute
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    ketogenic = models.BooleanField(default=False)
    pescetarian = models.BooleanField(default=False)
    peleo = models.BooleanField(default=False)

    def __str__(self):
        return self.preferences_id


class Meals(models.Model):
    breakfast = models.BooleanField(default=False)
    lunch = models.BooleanField(default=False)
    dinner = models.BooleanField(default=False)
    dessert = models.BooleanField(default=False)
    snack = models.BooleanField(default=False)

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
    intolorences = ArrayField(ArrayField(models.CharField(max_length=50)))
    budget = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.user_id
