from django.db import models
import jsonfield
# Create your models here.
from common.models import LogsMixin
from django.db.models import TextChoices
from user.models import Customer,User

class JobStatusChoices(TextChoices):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3


class Job(LogsMixin):
    job_name = models.CharField(max_length=300, null=True, blank=True)
    pickup_location = models.CharField(max_length=300, null=True, blank=True)
    dropoff_location = models.CharField(max_length=300, null=True, blank=True)
    pickup_location_coordinates = jsonfield.JSONField()
    dropoff_location_coordinates = jsonfield.JSONField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name="driver_jobs")
    job_status = models.CharField(max_length=200,null=True,blank=True,choices=JobStatusChoices.choices,default=JobStatusChoices.PENDING)

    def __str__(self):
        return self.job_name
