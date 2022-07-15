from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from .models import Preferences, Diet, Meals, MealHistory
import json


# home route
def home(request):
    return JsonResponse({'message': 'Welcome to the server'})


# login route
def user_login(request):
    # gets response from FE
    user_information = json.loads(request.body)
    email = user_information['email']
    password = user_information['password']
    # authenticate user
    user = authenticate(request, email=email, password=password)
    # check user exists
    if user is not None:
        login(request, user)
        return JsonResponse({'message': 'login successful'})
    else:
        return JsonResponse({'error': 'login unsuccessful'})


# logout route
def user_logout(request):
    # to be deleted when we can log in
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    #########
    logout(request)
    return JsonResponse({'message': 'User logged out'})


# create a new user route
def new_user(request):
    # get information from FE
    user_information = json.loads(request.body)
    # create user with data
    User.objects.create_user(
        username=user_information['name'], email=user_information['email'], password=user_information['password'])
    return JsonResponse({'message': 'user successfully created'})


# create preferences
def create_prefs(request):
    # to be deleted when we can log in
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    #########
    # check if user is logged in
    if request.user.is_authenticated:
        # get data from FE
        information = json.loads(request.body)
        # get user information
        user = request.user

        # split up the data
        pref_information = information['prefs']
        meal_info = information['meals']
        diet_information = information['diet']

        # create preferences
        Preferences.objects.create(
            user_id=user,
            calories_limit=pref_information['calories_limit'], intolorences=pref_information[
                'intolorences'], budget=pref_information['budget']
        )

        # create meals
        meals = Meals.objects.create(user_id=user,
                                     breakfast=meal_info['breakfast'], lunch=meal_info['lunch'], dinner=meal_info['dinner'],
                                     dessert=meal_info['dessert'], snack=meal_info[
                                         'snack']
                                     )

        # create diets
        diet = Diet.objects.create(user_id=user,
                                   vegan=diet_information['vegan'], vegetarian=diet_information[
                                       'vegetarian'], gluten_free=diet_information['glutenfree'],
                                   ketogenic=diet_information['ketogenic'], pescetarian=diet_information[
                                       'pescetarian'], paleo=diet_information['paleo']
                                   )
        # update preferences with diet and meal
        Preferences.objects.filter(user_id=user).update(
            diet_id=diet, meals_id=meals)

        return JsonResponse({'message': 'Preferences successfully added'})
    else:
        return JsonResponse({'error': 'User not authenticated'})


# update preferences
def update_pref(request):
    # to be deleted when we can log in
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    #########
    # check if user is logged in
    if request.user.is_authenticated:
        # get user information
        user = request.user

        if request.method == 'PATCH':
            # get information from FE
            information = json.loads(request.body)

            # Split data up
            pref_information = information['prefs']
            meal_info = information['meals']
            diet_information = information['diet']

            # update preferences
            Preferences.objects.filter(user_id=user).update(calories_limit=pref_information['calories_limit'], intolorences=pref_information[
                'intolorences'], budget=pref_information['budget'])

            # update meals
            Meals.objects.filter(user_id=user).update(breakfast=meal_info['breakfast'], lunch=meal_info['lunch'], dinner=meal_info['dinner'],
                                                      dessert=meal_info['dessert'], snack=meal_info['snack'])

            # update diet
            Diet.objects.filter(user_id=user).update(user_id=user, vegan=diet_information['vegan'], vegetarian=diet_information['vegetarian'], gluten_free=diet_information['glutenfree'], ketogenic=diet_information['ketogenic'], pescetarian=diet_information[
                'pescetarian'], paleo=diet_information['paleo'])

        return JsonResponse({'message': 'Preferences successfully updated'})
    else:
        return JsonResponse({'error': 'User not authenticated'})


# set meal history
def meal_history(request):
    # to be deleted when we can log in
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    #########
    # check if user is logged in
    if request.user.is_authenticated:
        # get information from FE
        meal_info = json.loads(request.body)
        # get user information
        user = request.user
        # create meal history object
        MealHistory.objects.create(
            user_id=user, recipes=meal_info['recipes']
        )
        return JsonResponse({'message': 'Meal history successfully added'})
    else:
        return JsonResponse({'error': 'User not authenticated'})


def get_meal_history(request):
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    if request.user.is_authenticated:
        user = request.user
        qs = MealHistory.objects.filter(user_id=user).values('recipes', 'date')
        print(qs)
        # qs_json = serializers.serialize('json', qs)
        # print(qs_json)
        return HttpResponse(qs,  content_type='application/json')
