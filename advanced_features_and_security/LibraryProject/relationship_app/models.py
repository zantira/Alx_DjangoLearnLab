from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager


# Create relationshipp_app models.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    #add permissions
    class Meta:
        permissions = [('can_add_book', 'can add a new book'), ('can_change_book', 'can change a book'), ('can_delete_book', 'can delete a book')]
    
    
    def __str__(self):
        return f"{self.title}; {self.author}"

class Library(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book)
    
    def __str__(self):
        return self.name
    

class Librarian(models.Model):
    name = models.CharField(max_length=200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name
    
    
#create user profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class Role(models.TextChoices):
        ADMIN = 'ADMINSTRATOR', 'Admin'
        MEMBER = 'MEMBER', 'Member'
        LIBRARIAN = 'LIBRARIAN', 'Librarian'
    role = models.CharField(
        max_length=12,
        choices=Role.choices,
        default=Role.MEMBER
    )
    
    def __str__(self):
        return f'{self.user.username} - {self.role}'


#Set up signals to autocreate Userprofile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

#define custom user manager
class CustomUserManger(BaseUserManager):
    
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
    email          =  models.EmailField(unique=True)
    profile_photo  =  models.ImageField(blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManger()
    
    
    def __str__(self):
        return self.email


        
    