from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Preferences, Diet, Meals, MealHistory
import json

# need to get the login in for

# home route


def home(request):
    return JsonResponse({'message': 'Welcome to the server'})


def my_view(request):
    user_information = json.loads(request.body)
    username = user_information['username']
    password = user_information['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

    else:
        return JsonResponse({'error': 'login unsuccessful'})
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


def meals(request):
    meal_info = json.loads(request.body)
    print(meal_info)
    Meals.objects.create(
        breakfast=meal_info['breakfast'], lunch=meal_info['lunch'], dinner=meal_info['dinner'],
        dessert=meal_info['dessert'], snack=meal_info[
            'snack']
    )
    return JsonResponse({'message': 'Meals successfully added'})


# def meal_history(request):
#     meal_info = json.loads(request.body)
#     # user = request.user
#     print(meal_info)
#     MealHistory.objects.create(
#         user_id=meal_info['user_id'], recipes=meal_info['recipes']
#     )
#     return JsonResponse({'message': 'Meals successfully added'})

def meal_history(request):
    if request.user.is_authenticated:
        meal_info = json.loads(request.body)
        user = request.user
        MealHistory.objects.create(
            user_id=user, recipes=meal_info['recipes']
        )
        return JsonResponse({'message': 'Meals successfully added'})
