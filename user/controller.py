from rest_framework.response import Response
from .serializer import *
from .models import *

class UserController():
    def get_user(self,request,id):
        users = User.objects.get(id=1)
        serializer = GetUSerSerializer(users,many=False)
        return Response(serializer.data,200)
        
    
    def signup(self,request):
        users = User.objects.get(id=1)
        serializer = SignupSerializer(users,many=False)
        return Response(serializer.data,200)