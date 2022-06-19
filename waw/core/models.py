from django.db import models

# Create your models here.
class Profile(models.Model):
   user_name = None
   user_id = None
   bio = None
   picture = models.ImageField('')
   location = None 
