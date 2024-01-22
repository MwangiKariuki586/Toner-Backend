from rest_framework import serializers
from .models import *

class Toner_RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toner_Request
        fields = ['Staff_name','Staff_ID','Department','Location','Toner_name','printer_name']

class Departments_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Kenindia_Department
        fields = ['Department_name']

class Location_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Kenindia_Location
        fields = ['Location_name']

class Printer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = ['Printer_name']

class Toner_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Toner
        fields = ['Toner']

