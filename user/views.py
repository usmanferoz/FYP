from django.shortcuts import render
from rest_framework.views import APIView
from .controller import *
from rest_framework.permissions import AllowAny


controller = UserController()

class UserApi(APIView):
    def get(self,request,id=None):
        return controller.get_user(request=request,id=id)
    def post():
        pass
    def patch(self,id=None):
        pass
    def delete(self,id=None):
        pass
    


class SignupApi(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        return controller.signup(request=request)