from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import Preferences, Diet, Meals, MealHistory
import json


# home route
def home(request):
    return JsonResponse({'message': 'Welcome to the server'})

# login route


def user_login(request):
    user_information = json.loads(request.body)
    username = user_information['username']
    password = user_information['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'message': 'login successful'})

    else:
        return JsonResponse({'error': 'login unsuccessful'})
        # this function creates a new user, it takes in name, email and password as json


def user_logout(request):
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    logout(request)
    return JsonResponse({'message': 'User logged out'})


def new_user(request):
    user_information = json.loads(request.body)
    User.objects.create_user(
        username=user_information['name'], email=user_information['email'], password=user_information['password'])
    return JsonResponse({'message': 'user successfully created'})


def new_pref(request):
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    user = request.user
    pref_information = json.loads(request.body)
    Preferences.objects.create(
        user_id=user,
        calories_limit=pref_information['calories_limit'], intolorences=pref_information[
            'intolorences'], budget=pref_information['budget']
    )
    return JsonResponse({'message': 'Preferences successfully added'})


def diet(request):
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    user = request.user
    diet_information = json.loads(request.body)
    diet = Diet.objects.create(user_id=user,
                               vegan=diet_information['vegan'], vegetarian=diet_information[
                                   'vegetarian'], gluten_free=diet_information['glutenfree'],
                               ketogenic=diet_information['ketogenic'], pescetarian=diet_information[
                                   'pescetarian'], paleo=diet_information['paleo']
                               )
    Preferences.objects.filter(user_id=user).update(
        diet_id=diet)
    return JsonResponse({'message': 'Diet successfully added'})


def meals(request):
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    user = request.user
    meal_info = json.loads(request.body)
    meals = Meals.objects.create(user_id=user,
                                 breakfast=meal_info['breakfast'], lunch=meal_info['lunch'], dinner=meal_info['dinner'],
                                 dessert=meal_info['dessert'], snack=meal_info[
                                     'snack']
                                 )
    Preferences.objects.filter(user_id=user).update(meals_id=meals)
    return JsonResponse({'message': 'Meals successfully added'})


def meal_history(request):
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    if request.user.is_authenticated:
        meal_info = json.loads(request.body)
        user = request.user
        MealHistory.objects.create(
            user_id=user, recipes=meal_info['recipes']
        )
        return JsonResponse({'message': 'Meal history successfully added'})
    else:
        return JsonResponse({'error': 'User not authenticated'})
