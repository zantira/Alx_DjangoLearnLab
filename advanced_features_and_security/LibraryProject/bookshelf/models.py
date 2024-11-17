from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} {self.author}, {self.publication_year}"
    
    
#define custom user manager
class CustomUserManager(BaseUserManager):
    
    def creat_user(self, email, password, profile_photo=None, **extra_fields):
        if not email:
            raise ValueError(_('You must add an email address'))
        email = self.normalize_email(email)
        user  = self.model(email=email, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    #create superuser
    def create_superuser(self, email, password, profile_photo=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        #validate superuser
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')
        
        return self.create_user(email, password, profile_photo, **extra_fields)

#create custom user model by extending AbstractUser
class CustomUser(AbstractUser):
    date_of_birth  =  models.DateField()
    profile_photo  =  models.ImageField(blank=True, null=True)
    email          = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager
    
    
    def __str__(self):
        return self.email