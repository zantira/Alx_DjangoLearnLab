from django.db import models
from django.contrib.auth.models import User


# Create relationshipp_app models.
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
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


from django.db.models.signals import post_save
from django.dispatch import receiver

#Set up signals to autocreate Userprofile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


