from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, ProfileImage

admin.site.register(Account)
admin.site.register(ProfileImage)