from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import TextChoices
from common.models import LogsMixin
# Create your models here.
class UserTypeChoices(TextChoices):
    ADMIN = 1
    EMPLOYEE = 2

class Customer(LogsMixin):
     company_name = models.CharField(max_length=300, null=True, blank=True)
     company_address = models.CharField(max_length=300, null=True, blank=True)

class User(AbstractUser):
    user_type = models.CharField(max_length=10, null=True, blank=True, choices=UserTypeChoices.choices,
                                 default=UserTypeChoices.ADMIN)
    email = models.EmailField(null=True, blank=True, unique=True)
    username = models.CharField(max_length=300, null=True, blank=True)
    password = models.CharField(max_length=1000, null=True, blank=True)
    avatar = models.ImageField(upload_to="user-avatar/", null=True, blank=True)
    login_token = models.TextField(null=True, blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    cnic = models.CharField(max_length=10000, null=True, blank=True)
    contact = models.CharField(max_length=10000, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
