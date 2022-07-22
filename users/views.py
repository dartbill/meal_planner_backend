from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.core import serializers
from itertools import chain
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
    username = User.objects.get(email=email.lower()).username
    # authenticate user
    user = authenticate(request, username=username, password=password)
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
    # #########
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
        print(pref_information)
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


# update and get preferences
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
        elif request.method == "GET":
            qs = Preferences.objects.filter(user_id=user).values(
                'calories_limit', 'intolorences', 'budget')
            qs2 = Meals.objects.filter(user_id=user).values(
                'breakfast', 'lunch', 'dinner', 'dessert', 'snack')
            # result_list = list(chain(qs, qs2))
            # print(result_list)
            return JsonResponse(qs, safe=False)
    else:
        return JsonResponse({'error': 'User not authenticated'})


# set and get meal history
def meal_history(request):
    # to be deleted when we can log in
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    #########
    # check if user is logged in
    if request.user.is_authenticated:
        # get information from FE
        user = request.user
        if request.method == 'POST':
            meal_info = json.loads(request.body)
            # create meal history object
            MealHistory.objects.create(
                user_id=user, today_date=meal_info['today_date'], recipes=meal_info['recipes']
            )
            return JsonResponse({'message': 'Meal history successfully added'})
        elif request.method == 'GET':
            # user = request.user
            # print(user)
            qs = MealHistory.objects.filter(
                user_id=user).values('recipes', 'today_date')
            # result_list = list(qs)
            # return JsonResponse(result_list, safe=False)
            qs_json = serializers.serialize('json', qs)
            return HttpResponse(qs_json, content_type='application/json')
    else:
        return JsonResponse({'error': 'User not authenticated'})


# send email to user
def send_email(request):
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    if request.user.is_authenticated:
        user = request.user
        email_info = json.loads(request.body)
        send_mail(
            subject='From Django',
            message=email_info['message'],
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
            html_message=email_info['html']
        )
        return JsonResponse({'message': 'email sent successfully'})


def delete_meal(request):
    user1 = authenticate(request, username='billie', password='Hello')
    if user1 is not None:
        login(request, user1)
    #########
    # check if user is logged in
    if request.user.is_authenticated:
        if request.method == "DELETE":
            user = request.user
            qs = MealHistory.objects.filter(
                user_id=user).first().delete()
    else:
        return JsonResponse({'error': 'User not authenticated'})
