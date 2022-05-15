from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('signupFun',signupFun,name='signupFun'),
    path('login',login,name='login'),
    path('dashboard',dashboard,name='dashboard'),
    path('logout',logout,name='logout')







]
