from django.contrib import admin
from django.urls import path
from user.views import *

app_name = "user"

urlpatterns = [
    path('login/', loginUser, name = "login"),
    path('register/', register, name = "register"),
    path('logout/', logoutUser, name = "logout"),
]
