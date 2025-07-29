from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import AccountManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from misc.models import *

class Account(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = AccountManager()
    
    image = models.ImageField(upload_to='Profile Images', null=True)
    bio = models.TextField(null=True)

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_agent = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    address = models.CharField(max_length=250, null=True)
    
    def __str__(self):
        return self.email
    
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
