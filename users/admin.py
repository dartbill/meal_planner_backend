from django.contrib import admin

# Register your models here.
from .models import Preferences, Diet, Meals, MealHistory

admin.site.register(Preferences)
admin.site.register(Diet)
admin.site.register(Meals)
admin.site.register(MealHistory)
