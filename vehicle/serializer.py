
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Vehicle , VehicleAllocation

class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'



class VehicleAllocationSerializer(ModelSerializer):
    class Meta:
        model = VehicleAllocation
        fields = '__all__'

    def to_representation(self, instance):
        data = dict()
        data['id'] = instance.id
        data['vehicle_name'] = instance.vehicle.vehicle_name
        data['vehicle_number'] = instance.vehicle.vehicle_number
        data['emoloyee_email'] = instance.employee.email
        data['empolyee_type'] = instance.employee.user_type
        data['empolyee_id'] = instance.employee.id
        data['employee_name'] = instance.employee.first_name

        return data