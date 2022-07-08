from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
 
 
class User(AbstractUser):
    username = models.CharField(unique=True,max_length=1000)
    email = models.EmailField()
    phone = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    