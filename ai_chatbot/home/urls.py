from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.chat),
    path('chatapi',views.chatapi),
    path('chatbot',views.chatbot),
    path('login',views.chatbot_login, name='login'),
    path('register',views.chatbot_register, name='register'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('lgout',views.lgout, name='lgout'),
    path('delete_chat',views.delete_chat, name='delete_chat'),
    path('history',views.history, name='history'),



]