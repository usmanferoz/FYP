from rest_framework.serializers import ModelSerializer
from .models import *

class GetUSerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'