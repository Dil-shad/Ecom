from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [

    path('', index, name='index'),
    path('detail_view/<int:pk>', detail_view, name='detail_view'),
    path('profile', profile, name='profile'),
    path('signupFun', signupFun, name='signupFun'),
    path('login', login, name='login'),
    #--------------ADMIN--------------#
    path('dashboard', dashboard, name='dashboard'),
    path('delete_usr/<int:pk>', delete_usr, name='delete_usr'),
    path('admin_cart_view/<int:pk>', admin_cart_view, name='admin_cart_view'),
    path('ProductModelEdit/<int:pk>', ProductModelEdit, name='ProductModelEdit'),
    path('delete_product/<int:pk>',delete_product,name='delete_product'),


    #-----------------------------------#
    path('logout', logout, name='logout'),
    path('add_category', add_category, name='add_category'),
    path('cart', cart, name='cart'),
    path('add_to_cart/<int:pk>', add_to_cart, name='add_to_cart'),
    path('remove_cart/<int:pk>', remove_cart, name='remove_cart'),
    #------------ shopping panel--------------------#

    path('shop_panel', shop_panel, name='shop_panel'),

    #-------------------filtering pages----------------#

    path('laptop_filter', laptop_filter, name='laptop_filter'),
    path('tv_filter', tv_filter, name='tv_filter'),
    path('home_filter', home_filter, name='home_filter'),
    path('fitness_filter', fitness_filter, name='fitness_filter'),
    path('redmi_filter', redmi_filter, name='redmi_filter'),
    path('audio_filter', audio_filter, name='audio_filter'),

    path('about', about, name='about'),






]
