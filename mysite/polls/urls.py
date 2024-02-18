from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Entry/', views.polls, name='Entry'),
    # path('home/', views.home, name='home'),  # Use a single URL pattern for the home page
    path('login/', views.login, name='login'),
    path('Registration/', views.Registration, name='Registration'),
    path('EmpR/', views.EmpRegistration, name='EmpRegistration'),
    path('EmpL/', views.EmpLogin, name='EmpLogin'),
    path('defaultpg/', views.defaultpg, name='defaultpg'),
    path('emphome/', views.emphome, name= 'emphome'),
    path('chome/', views.chome, name= 'chome'),
    path('ehome/', views.ehome, name= 'ehome'),
    path('loginverify/', views.loginverify, name= 'loginverify'),
    path('emploginverify/', views.emploginverify, name= 'emploginverify'),
    path('buy/', views.buy, name= 'buy'),
    path('service/', views.service, name= 'service'),
    path('eservice/', views.eservice, name= 'eservice'),
    path('event/', views.events, name= 'events'),
    path('servicereq/', views.servicereq, name= 'servicereq'),
    path('getservice/', views.getservice, name= 'getservice'),
    





]
