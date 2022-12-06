
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User

class UserLoginSerializer(ModelSerializer):
    full_name = serializers.SerializerMethodField("get_name")

    def get_name(self,object):
        try:
            return object.customer.company_name
        except Exception as e:
            print(e)
            return None
    class Meta:
        model = User
        fields = ['id','email','full_name','customer_id']


class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'first_name', 'last_name' , 'customer' , 'user_type', 'contact' , 'cnic']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'username', 'first_name', 'last_name' , 'customer' , 'user_type' , 'contact' , 'cnic']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        user.save()
        return user
