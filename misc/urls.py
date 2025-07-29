from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('countries/', CountriesView.as_view()),
    path('regions/', RegionsView.as_view()),
    path('areas/', AreasView.as_view()),
]