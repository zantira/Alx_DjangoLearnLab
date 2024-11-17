from django.contrib.auth.models import User
#create a new user
user = User.objects.create_user(username='Chris', password='Chriz6972766')
user.email = 'jeremyzantira@gmail.com'
user.save()