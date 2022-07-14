from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse
import json

# create_user(username, email=None, password=None, **extra_fields)¶
# Create your views here.
# def create_cat(request):
#     if request.method == 'POST':
#         new_cat = json.loads(request.body)
#         Cat.objects.create(name=new_cat['name'], age=new_cat['age'])
#     return JsonResponse({'message': 'Cat successfully created'})
# {
#     "name": 'name',
#     'email': 'email',
#     'password':'password'
# }


def new_user(request):
    user_information = json.loads(request.body)
    print(user_information)
    User.objects.create_user(
        username=user_information['name'], email=user_information['email'], password=user_information['password'])
    return JsonResponse({'message': 'user successfully created'})
