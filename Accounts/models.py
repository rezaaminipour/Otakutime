from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from django import forms



class CustomUser(AbstractUser):
    
    username         = models.CharField(max_length=100 , blank=True)
    email            = models.EmailField(_('email address'), unique=True)
    first_name       = models.CharField(max_length=30,blank=True)
    last_name        = models.CharField(max_length=50,blank=True)
    date_of_birth    = models.DateField(blank=True,null=True)

    profile_image    = models.ImageField(upload_to='profiles/image/',blank=True,default='image/Otaku.jpg' )
    background_image = models.ImageField(upload_to='profiles/image/',blank=True,default='image/Otaku.jpg' )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email





