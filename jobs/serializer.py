
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Job , JobStatusChoices

class JobSerializer(ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


    def to_representation(self, instance):
        data = dict()
        data['id'] = instance.id
        data['job_name'] = instance.job_name
        data['pickup_location'] = instance.pickup_location
        data['dropoff_location'] = instance.dropoff_location
        data['pickup_location_coordinates'] = instance.pickup_location_coordinates
        data['dropoff_location_coordinates'] = instance.dropoff_location_coordinates
        data['job_status'] = instance.job_status
        data['driver_id'] = instance.driver_id
        data['driver_name'] = instance.driver.first_name
        data['customer_id'] = instance.driver.customer_id
        data['created_at'] = instance.created_at

        return data
