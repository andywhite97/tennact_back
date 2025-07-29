from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', ListingsView.as_view()),
    path('<int:pk>/', SingleListingView.as_view()),
    path('conditions/', ConditionsView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('types/', PropertyTypesView.as_view()),
    
    path('image/upload/', ImageUploadView.as_view()),

]