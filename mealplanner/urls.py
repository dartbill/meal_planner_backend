"""mealplanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pdb import post_mortem
from webbrowser import get
from django.contrib import admin
from django.urls import path
from users.views import home, new_user, meal_history, user_login, user_logout, create_prefs, update_pref, send_email, delete_meal

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('createuser/', new_user),
    path('mealhistory/', meal_history),
    path('login/', user_login),
    path('createprefs/', create_prefs),
    path('prefs/', update_pref),
    path('logout/', user_logout),
    path('delete/', delete_meal),
    path('email/', send_email)
]
