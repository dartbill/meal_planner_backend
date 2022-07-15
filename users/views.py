from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
import json

# {
#     "name": 'name',
#     'email': 'email',
#     'password':'password'
# }

# this function creates a new user, it takes in name, email and password as json


def home(request):
    return JsonResponse({'message': 'Welcome to the server'})


def new_user(request):
    user_information = json.loads(request.body)
    print(user_information)
    User.objects.create_user(
        username=user_information['name'], email=user_information['email'], password=user_information['password'])
    return JsonResponse({'message': 'user successfully created'})


def new_pref(request):
    pref_information = json.loads(request.body)
    print(pref_information)
    User.objects.create_pref(
        user_id=pref_information['user_id'], diet_id=pref_information['diet_id'], meals_id=pref_information['meals_id'],
        calores_limit=pref_information['calories_limit'], intolorences=pref_information[
            'intolorences'], budget=pref_information['budget']
    )
    return JsonResponse({'message': 'Preferences successfully added'})
