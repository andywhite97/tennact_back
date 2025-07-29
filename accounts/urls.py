from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

from .views import *

urlpatterns = [
    path('', AccountList.as_view()),
    path('register/', RegisterView.as_view()),
    path('auth/', views.obtain_auth_token)
]