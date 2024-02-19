from rest_framework import serializers

from custom_auth.models import CustomUser, Kenindia_Department, Kenindia_Location, Printer, Toner, Toner_Request
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email'] 
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('staff_id', 'password')

class Toner_RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toner_Request
        fields = '__all__'
    def create(self, validated_data):
        # Access the request object and extract user-related information
        request = self.context.get('request')
        if request:
            user = request.user
            validated_data['user_staffid'] = user.staffid
            validated_data['user_staffname'] = user.staff_name
            validated_data['user_department'] = user.department.Department_name if user.department else None
            validated_data['user_location'] = user.location.Location_name if user.location else None
             # Validate 'toner' and 'printer_name'
            if not validated_data.get('toner'):
                raise serializers.ValidationError("'toner' is a required field.")
            if not validated_data.get('printer_name'):
                raise serializers.ValidationError("'printer_name' is a required field.")

        # Create and return the Toner_Request instance
        return Toner_Request.objects.create(**validated_data)

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
        fields = '__all__'

# class UserSerializer(serializers.ModelSerializer):
#     username=serializers.CharField(max_length = 500)
#     password=serializers.CharField(max_length = 500,write_only=True)
#     access_token=serializers.CharField(max_length = 500,read_only=True)
#     refresh_token=serializers.CharField(max_length = 500,read_only=True)
#     class Meta():
#         model = User
#         fields = ['username','password','access_token','refresh_token']

#     def validate(self, attrs):
#         username=attrs.get('email')
#         password = attrs.get('password')
#         request=self.context.get('request')
#         user = authenticate(request, username=username,password=password)
#         if not user:
#             raise AuthenticationFailed("invalid credentials try again")
#         token = user.tokens()

#         return {
#             'username':user.username,
#             'access_token':user
#         }
    

