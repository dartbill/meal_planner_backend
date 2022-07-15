from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Preferences, Diet, Meals, MealHistory
import json

# need to get the login in for

# home route


def home(request):
    return JsonResponse({'message': 'Welcome to the server'})


# this function creates a new user, it takes in name, email and password as json
def new_user(request):
    user_information = json.loads(request.body)
    print(user_information)
    User.objects.create_user(
        username=user_information['name'], email=user_information['email'], password=user_information['password'])
    return JsonResponse({'message': 'user successfully created'})


def new_pref(request):
    pref_information = json.loads(request.body)
    print(pref_information)
    Preferences.objects.create(
        user_id=pref_information['user_id'], diet_id=pref_information['diet_id'], meals_id=pref_information['meals_id'],
        calories_limit=pref_information['calories_limit'], intolorences=pref_information[
            'intolorences'], budget=pref_information['budget']
    )
    return JsonResponse({'message': 'Preferences successfully added'})


def diet(request):
    diet_information = json.loads(request.body)
    print(diet_information)
    Diet.objects.create(
        vegan=diet_information['vegan'], vegetarian=diet_information['vegetarian'], gluten_free=diet_information['glutenfree'],
        ketogenic=diet_information['ketogenic'], pescetarian=diet_information[
            'pescetarian'], peleo=diet_information['peleo']
    )
    return JsonResponse({'message': 'Diet successfully added'})
