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


def new_user(request):
    user_information = json.loads(request.body)
    print(user_information)
    User.objects.create_user(
        username=user_information['name'], email=user_information['email'], password=user_information['password'])
    return JsonResponse({'message': 'user successfully created'})
