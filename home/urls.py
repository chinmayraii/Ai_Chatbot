from django.contrib import admin
from django.urls import path
from . import views
from . import api
from home.api import BotApi,RegisterAPIView


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
    path('profile',views.profile, name='profile'),
    path('add_profile',views.add_profile, name='add_profile'),
    path('delete_profile',views.delete_profile, name='delete_profile'),
    path('deactivate',views.deactivate, name='deactivate'),
    path('response_pdf',views.response_pdf,name='response_pdf'),

    # API urls
    path('api/register/', RegisterAPIView.as_view()),
    path('api/chatbot_api',BotApi.as_view(), name='api/chatbot_api')

]