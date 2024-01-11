from rest_framework import serializers
from .models import *

class Toner_RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toner_Request
        fields = ['Staff_name','Staff_ID','Department','Location','Toner_name','printer_name']