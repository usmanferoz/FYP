from django.db import models
from common.models import LogsMixin
from user.models import Customer,User
# Create your models here.
import jsonfield


class Vehicle(LogsMixin):
    vehicle_name = models.CharField(max_length=300, null=True, blank=True)
    vehicle_number = models.CharField(max_length=300, null=True, blank=True)
    vehicle_model = models.CharField(max_length=300, null=True, blank=True)
    vehicle_company = models.CharField(max_length=300, null=True, blank=True)
    avatar = models.ImageField(upload_to="vehicle-avatar/", null=True, blank=True)
    vehicle_last_location = jsonfield.JSONField()
    chassis_no = models.CharField(max_length=300, null=True, blank=True)

    vehicle_fuel = models.CharField(max_length=300, null=True, blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    colour = models.CharField(max_length=300, null=True, blank=True)
    milage = models.CharField(max_length=300, null=True, blank=True)
    def __str__(self):
        return self.vehicle_name



class VehicleAllocation(LogsMixin):
    employee = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE,null=True,blank=True)