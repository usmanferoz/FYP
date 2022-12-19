from django.shortcuts import render
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
from .models import Vehicle , VehicleAllocation
from .serializer import VehicleSerializer , VehicleAllocationSerializer
from django.db.models import F , Prefetch

# Create your views here.

class VehicleApiView(ModelViewSet):
    authentication_classes = [UserAuthentication]
    permission_classes = []
    model = Vehicle
    serializer_class = VehicleSerializer

    def get_listing(self, request):
        try:
            customer_id = request.user.customer_id

            if request.query_params.get("id"):
                vehicles = self.model.objects.filter(id=request.query_params.get("id"),customer_id=customer_id)
                if vehicles.exists():
                    serializer = self.serializer_class(vehicles.last(), many=False).data
                    return Response(create_resonse(False, Message.success.value, [serializer]))
                return Response(create_resonse(True, Message.record_not_found.value, []))

            vehicles = self.model.objects.filter(customer_id=customer_id)
            if vehicles.exists():
                serializer = self.serializer_class(vehicles,many=True).data
                return Response(create_resonse(False, Message.success.value, serializer))
            return Response(create_resonse(True, Message.record_not_found.value, []))
        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, []))

    def create_vehicle(self, request):
        try:
            request.data['customer'] = request.user.customer_id
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
            return Response(create_resonse(True, Message.try_with_correct_data.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))

    def edit_vehicle(self, request):
        try:
            if not request.data.get("id"):
                return Response(create_resonse(False, Message.query_params_missing.value, []))
            vehicle = self.model.objects.filter(id=request.data.get("id"))
            if vehicle.exists():
                serialized_data = self.serializer_class(vehicle.last(),data=request.data,partial=True)
                if serialized_data.is_valid():
                    serialized_data.save()
                    return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
                return Response(create_resonse(True, Message.try_with_correct_data.value, []))
            return Response(create_resonse(True, Message.record_not_found.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))

    def delete_vehicle(self, request):
        try:
            if not request.query_params.get("id"):
                return Response(create_resonse(False, Message.query_params_missing.value, []))
            vehicle = self.model.objects.filter(id=request.query_params.get("id"))
            if vehicle.exists():
                vehicle.delete()
                return Response(create_resonse(False, Message.success.value, []))
            return Response(create_resonse(True, Message.record_not_found.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))


    def get_driver_vehicle(self,request):
        try:
            if not request.query_params.get("user_id"):
                return Response(create_resonse(False, Message.query_params_missing.value, []))
            user = request.query_params.get("user_id")
            driver_vehicle = VehicleAllocation.objects.filter(employee_id = request.query_params.get("user_id"))
            if driver_vehicle.exists():
                vehicle = self.model.objects.filter(id = driver_vehicle.last().vehicle_id)
                if vehicle.exists():
                    serialized_data = self.serializer_class(vehicle.last(),many=False).data
                    return Response(create_resonse(False,Message.success.value,[serialized_data]))
                return Response(create_resonse(False,Message.record_not_found.value,[]))
            return Response(create_resonse(False, Message.record_not_found.value, []))
        except Exception as e:
            print(e)
            return Response(create_resonse(True,Message.server_error.value,[]))


class VehicleAllocationApiView(ModelViewSet):
    authentication_classes = [UserAuthentication]
    permission_classes = []
    model = VehicleAllocation
    serializer_class = VehicleAllocationSerializer

    def get_listing(self, request):
        try:
            customer_id = request.user.customer_id
            if request.query_params.get("id"):
                allocation = self.model.objects.filter(id=request.query_params.get("id"),customer_id=customer_id)
                if allocation.exists():
                    serializer = self.serializer_class(allocation.last(), many=False).data
                    return Response(create_resonse(False, Message.success.value, [serializer]))
                return Response(create_resonse(True, Message.record_not_found.value, []))

            allocations = self.model.objects.filter(customer_id=customer_id)
            if allocations.exists():
                serializer = self.serializer_class(allocations,many=True).data
                return Response(create_resonse(False, Message.success.value, serializer))
            return Response(create_resonse(True, Message.record_not_found.value, []))
        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, []))

    def create_allocation(self, request):
        try:
            request.data['customer'] = request.user.customer_id
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
            return Response(create_resonse(True, Message.try_with_correct_data.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))

    def edit_allocation(self, request):
        try:
            if not request.data.get("id"):
                return Response(create_resonse(False, Message.query_params_missing.value, []))
            allocation = self.model.objects.filter(id=request.data.get("id"))
            if allocation.exists():
                serialized_data = self.serializer_class(allocation.last(),data=request.data,partial=True)
                if serialized_data.is_valid():
                    serialized_data.save()
                    return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
                return Response(create_resonse(True, Message.try_with_correct_data.value, []))
            return Response(create_resonse(True, Message.record_not_found.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))

    def delete_allocation(self, request):
        try:
            if not request.query_params.get("id"):
                return Response(create_resonse(False, Message.query_params_missing.value, []))
            allocation = self.model.objects.filter(id=request.query_params.get("id"))
            if allocation.exists():
                allocation.delete()
                return Response(create_resonse(False, Message.success.value, []))
            return Response(create_resonse(True, Message.record_not_found.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))