from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_list_or_404
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
class MyTokenObtainPairview(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
@api_view(['GET','POST'])
def Toner_requests(request):
    if request.method == 'GET':
        requests_toners = Toner_Request.objects.all()
        serializer =  Toner_RequestSerializer(requests_toners, many = True)
        return JsonResponse({"Toner_requests":serializer.data})

    if request.method == 'POST':
        serializer = Toner_RequestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

def Toners_view(request):
    toners = Toner.objects.all()
    serializer =  Toner_Serializer(toners, many = True)
    return JsonResponse({"Toners":serializer.data})

def Printer_view(request):
    printers = Printer.objects.all()
    serializer =  Printer_Serializer(printers, many = True)
    return JsonResponse({"Printer":serializer.data})

def Department_view(request):
    departments = Kenindia_Department.objects.all()
    serializer =  Departments_Serializer(departments, many = True)
    return JsonResponse({"Departments":serializer.data})

def Location_view(request):
    locations = Kenindia_Location.objects.all()
    serializer = Location_Serializer(locations, many = True)
    return JsonResponse({"Locations":serializer.data})

# class loginView(GenericAPIView):
#     serializer_class = UserSerializer
#     def post(self,request):
#         serializer = self.serializer_class(data = request.data)
#         serializer.is_valid(raise_exception = True)
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
    ]
    return Response(routes)