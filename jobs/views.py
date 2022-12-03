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
from .models import Job , JobStatusChoices
from .serializer import JobSerializer
from django.db.models import F, Prefetch
from django.shortcuts import render

# Create your views here.


class JobApiView(ModelViewSet):
    authentication_classes = [UserAuthentication]
    permission_classes = []
    model = Job
    serializer_class = JobSerializer

    def get_listing(self, request):
        try:
            customer_id = request.user.customer_id

            if request.query_params.get("id"):
                Jobs = self.model.objects.filter(id=request.query_params.get("id"),customer_id=customer_id)
                if Jobs.exists():
                    serializer = self.serializer_class(Jobs.last(), many=False).data
                    return Response(create_resonse(False, Message.success.value, [serializer]))
                return Response(create_resonse(True, Message.record_not_found.value, []))

            jobs = self.model.objects.filter(customer_id=customer_id)
            if jobs.exists():
                serializer = self.serializer_class(jobs,many=True).data
                return Response(create_resonse(False, Message.success.value, serializer))
            return Response(create_resonse(True, Message.record_not_found.value, []))
        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, []))

    def create_job(self, request):
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

    def edit_job(self, request):
        try:
            if not request.data.get("id"):
                return Response(create_resonse(False, Message.query_params_missing.value, []))
            job = self.model.objects.filter(id=request.data.get("id"))
            if job.exists():
                serialized_data = self.serializer_class(job.last(),data=request.data,partial=True)
                if serialized_data.is_valid():
                    serialized_data.save()
                    return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
                return Response(create_resonse(True, Message.try_with_correct_data.value, []))
            return Response(create_resonse(True, Message.record_not_found.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))

    def delete_job(self, request):
        try:
            if not request.query_params.get("id"):
                return Response(create_resonse(False, Message.query_params_missing.value, []))
            job = self.model.objects.filter(id=request.query_params.get("id"))
            if job.exists():
                job.delete()
                return Response(create_resonse(False, Message.success.value, []))
            return Response(create_resonse(True, Message.record_not_found.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))


    def driver_jobs(self, request):
        try:
            customer_id = request.user.customer_id
            if request.query_params.get("id"):
                Jobs = self.model.objects.filter(id=request.query_params.get("id"),customer_id=customer_id , driver = request.user.id)
                if Jobs.exists():
                    serializer = self.serializer_class(Jobs.last(), many=False).data
                    return Response(create_resonse(False, Message.success.value, [serializer]))
                return Response(create_resonse(True, Message.record_not_found.value, []))

            jobs = self.model.objects.filter(customer_id=customer_id , driver= request.user.id)
            if jobs.exists():
                serializer = self.serializer_class(jobs,many=True).data
                return Response(create_resonse(False, Message.success.value, serializer))
            return Response(create_resonse(True, Message.record_not_found.value, []))
        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, []))


