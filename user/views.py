from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
# Create your views here.
from django.utils import timezone
from common.models import StatusChoices
from common.baselayer.baseAuth import UserAuthentication
from common.helper import encode_token, create_resonse
from rest_framework.response import Response
from common.enums import Message
from .models import User , Customer
from .serializer import (
    UserLoginSerializer, UserSignupSerializer , UserSerializer )
from django.db.models import F , Prefetch
from jobs.models import Job
from vehicle.models import VehicleAllocation , Vehicle

class UserAuthView(ModelViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]
    model = User

    def login(self, request):
        try:
            user = self.model.objects.filter(email=request.data.get('email')).first()
            try:
                if user:
                    if not user.check_password(request.data.get("password")):
                        return Response(create_resonse(True, Message.incorrect_password.value, []))
                    data = UserLoginSerializer(user,many=False).data
                    data['token'] = encode_token(user)
                    user.login_token = data['token']
                    user.save()
                    return Response(create_resonse(False, Message.success.value, [data]))
                return Response(create_resonse(True, Message.user_not_exists.value, []))
            except Exception as e:
                print(e)
                return Response(create_resonse(True, Message.try_with_correct_data.value, []))
        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, []))

    def signup(self, request):
        try:
            if self.model.objects.filter(email=request.data.get("email")).exists():
                return Response(create_resonse(True, Message.email_exists.value, []))
            company_name = request.data.pop("company_name")
            company_address = request.data.pop("company_address")
            customer = Customer(company_name=company_name,company_address=company_address)
            customer.save()
            request.data['customer'] = customer.id
            serialized_data = UserSignupSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
            return Response(create_resonse(True, Message.try_with_correct_data.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))


class UserApiView(ModelViewSet):
    authentication_classes = [UserAuthentication]
    permission_classes = [AllowAny]
    model = User

    def get_listing(self, request):
        try:
            customer_id = request.user.customer_id
            if request.query_params.get("id"):
                users = self.model.objects.filter(id=request.query_params.get("id") , customer_id=customer_id)
                if users.exists():
                    serializer = UserSerializer(users.last(), many=False).data
                    return Response(create_resonse(False, Message.success.value, [serializer]))

            users = self.model.objects.filter(customer_id=customer_id)
            if users.exists():
                serializer = UserSerializer(users,many=True).data
                return Response(create_resonse(False, Message.success.value, serializer))
            return Response(create_resonse(True, Message.record_not_found.value, []))
        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, []))

    def create_user(self, request):
        try:
            if self.model.objects.filter(email=request.data.get("email")).exists():
                return Response(create_resonse(True, Message.email_exists.value, []))
            request.data['customer'] = request.user.customer_id
            serialized_data = UserSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
            return Response(create_resonse(True, Message.try_with_correct_data.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))

    def edit_user(self, request):
        try:
            if not request.data.get("id"):
                return Response(create_resonse(False, Message.query_params_missing.value, []))
            target_user = self.model.objects.filter(id=request.data.get("id"))
            if target_user.exists():
                serialized_data = UserSerializer(target_user.last(),data=request.data,partial=True)
                if serialized_data.is_valid():
                    serialized_data.save()
                    return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
            return Response(create_resonse(True, Message.user_not_exists.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))

    def delete_user(self, request):
        try:
            if not request.query_params.get("id"):
                return Response(create_resonse(False, Message.query_params_missing.value, []))
            target_user = self.model.objects.filter(id=request.query_params.get("id"))
            if target_user.exists():
                target_user.delete()
                return Response(create_resonse(False, Message.success.value, []))
            return Response(create_resonse(True, Message.user_not_exists.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))


    def get_dashboard(self,request):
        try:
            customer = request.user.customer_id
            data = {}
            total_users = self.model.objects.filter(customer_id = customer).all().count()
            total_jobs = Job.objects.filter(customer_id = customer).all().count()
            total_vehicles = Vehicle.objects.filter(customer_id = customer).all().count()
            total_vehicles_allocations = VehicleAllocation.objects.filter(customer_id = customer).all().count()
            data['total_users'] = total_users
            data['total_jobs'] = total_jobs
            data['total_vehicles'] = total_vehicles
            data['total_vehicles_allocations'] = total_vehicles_allocations
            return Response(create_resonse(False, Message.success.value, data=[data]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))
