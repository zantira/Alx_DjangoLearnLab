from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import  Group, Permission, User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} {self.author}, {self.publication_year}"
    
    
    
#define custom user manager
class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, username=None, profile_photo=None, **extra_fields):
        if not email:
            raise ValueError(_('You must add an email address'))
        email = self.normalize_email(email)
        user  = self.model(email=email, username=username, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    #create superuser
    def create_superuser(self, email, password, username=None, profile_photo=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        #validate superuser
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True')
        
        return self.create_user(email, password, username, profile_photo, **extra_fields)

#create custom user model by extending AbstractUser
class CustomUser(AbstractUser):
    first_name     = models.CharField(max_length=200)
    last_name      = models.CharField(max_length=200)
    date_of_birth  = models.DateField(verbose_name='Date of Birth')
    profile_photo  = models.ImageField(blank=True, null=True, verbose_name='Profile Photo')
    email          = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    
    def __str__(self):
        return self.email
    


# Create groups
editors_group, _ = Group.objects.get_or_create(name='Editors')
viewers_group, _ = Group.objects.get_or_create(name='Viewers')
admins_group, _ = Group.objects.get_or_create(name='Admins')

class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ('can_view', 'Can view post'),
            ('can_create', 'Can create post'),
            ('can_edit', 'Can edit post'),
            ('can_delete', 'Can delete post'),
        ]

# Assign permissions to groups
try:
    can_view = Permission.objects.get(codename='can_view')
    can_create = Permission.objects.get(codename='can_create')
    can_edit = Permission.objects.get(codename='can_edit')
    can_delete = Permission.objects.get(codename='can_delete')

    editors_group.permissions.add(can_view, can_create, can_edit)
    viewers_group.permissions.add(can_view)
    admins_group.permissions.add(can_view, can_create, can_edit, can_delete)

except Permission.DoesNotExist as e:
    print(f"Missing permission: {e}")

# Create a user and add to the Editors group
user = User.objects.create(username='john', email='john@gmail.com', password='johnpassword')
user.last_name = 'Lennon'
user.save()
user.groups.add(editors_group)

