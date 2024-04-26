from django.http import JsonResponse
from django.shortcuts import render
from .models import *
from custom_auth.models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_list_or_404
from rest_framework.generics import GenericAPIView
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET', 'POST'])  
# @permission_classes([IsAuthenticated])
def Toner_requests(request):
    if request.method == 'GET':
        requests_toners = Toner_Request.objects.all()
        serializer = Toner_RequestSerializer(requests_toners, many=True)
        return JsonResponse({"Toner_requests": serializer.data})

    if request.method == 'POST':
           # Set the user-related fields directly in the serializer
        data = {
            'user_staffid': request.user.staffid,
            'user_staffname': request.user.staff_name,
            'user_department': request.user.department.Department_name if request.user.department else None,
            'user_location': request.user.location.Location_name if request.user.location else None,
            'toner': request.data.get('toner'),  # Adjust based on your serializer
            'printer_name': request.data.get('printer_name'),  # Adjust based on your serializer
            'issued': False,
        }

        serializer = Toner_RequestSerializer(data=data, context={'request': request})

        if serializer.is_valid():
            #serializer.validated_data['user'] = request.user
            serializer.save()
            #print(f"Data sent from frontend: {serializer.data}")
            toner_request_data = serializer.data
            staff_id = toner_request_data.get('user_staffid', 'Unknown Staff ID')
            staff_name = toner_request_data.get('user_staffname', 'Unknown Staff Name')
            department = toner_request_data.get('user_department', 'Unknown Department')
            location = toner_request_data.get('user_location', 'Unknown Location')
            toner_id = toner_request_data.get('toner', None)
            
            # Fetch tonername using tonerid
            try:
                toner = Toner.objects.get(id=toner_id)
                toner_name = toner.Toner_name
            except Toner.DoesNotExist:
                toner_name = 'Unknown Toner Name'
            
            # Construct the email message
            subject = 'Toner Request'
            message = (
                f'Hello, there is a new toner request from:\n'
                f'Staff ID: {staff_id}\n'
                f'Staff Name: {staff_name}\n'
                f'Department: {department}\n'
                f'Location: {location}\n'
                f'For:\n'
                f'Toner Name: {toner_name}\n'
            )
            email_from = 'aleqohmwas@gmail.com'
            recipient_list = ['hurtlessemkay@gmail.com']
            try:
                # Send email
                send_mail(subject, message, email_from, recipient_list, fail_silently=False)
            except Exception as e:
                # Highlight: Logging the email sending issue
                print(f"Error sending email: {e}")

            # Highlight: Returning the serialized data for confirmation
            return Response({
                'message': 'Toner request sent successfully',
                'data_sent_from_frontend': serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            # Highlight: Returning detailed errors for better feedback
            return Response({
                'error': 'Toner request validation failed',
                'errors': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        #     send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def Toner_request_detail(request, pk):
    try:
        toner_request = Toner_Request.objects.get(pk=pk)
    except Toner_Request.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = Toner_RequestSerializer(toner_request)
    return Response(serializer.data)
def Toners_view(request):
    toners = Toner.objects.all()
    serializer =  Toner_Serializer(toners, many = True)
    return JsonResponse({"Toners":serializer.data})
@api_view(['GET'])
def Toner_detail(request, pk):
    try:
        toner = Toner.objects.get(pk=pk)
    except Toner.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = Toner_Serializer(toner)
    return Response(serializer.data)
def Printer_view(request):
    printers = Printer.objects.all()
    serializer =  Printer_Serializer(printers, many = True)
    return JsonResponse({"Printer":serializer.data})
@api_view(['GET'])
def Printer_detail(request, pk):
    try:
        printer = Printer.objects.get(pk=pk)
    except Printer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = Printer_Serializer(printer)
    return Response(serializer.data)
def Department_view(request):
    departments = Kenindia_Department.objects.all()
    serializer =  Departments_Serializer(departments, many = True)
    return JsonResponse({"Departments":serializer.data})
@api_view(['GET'])
def Department_detail(request, pk_or_name):
    try:
        # Try to lookup by ID first
        department = Kenindia_Department.objects.get(pk=pk_or_name)
    except (Kenindia_Department.DoesNotExist, ValueError):
        # If not found by ID, try to lookup by name
        try:
            department = Kenindia_Department.objects.get(Department_name=pk_or_name)
        except Kenindia_Department.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = Departments_Serializer(department)
    return Response(serializer.data)
def Location_view(request):
    locations = Kenindia_Location.objects.all()
    serializer = Location_Serializer(locations, many = True)
    return JsonResponse({"Locations":serializer.data})
@api_view(['GET'])
def Location_detail(request, pk_or_name):
    try:
        location = Kenindia_Location.objects.get(pk=pk_or_name)
    except (Kenindia_Location.DoesNotExist, ValueError):
        # If not found by ID, try to lookup by name
        try:
            location = Kenindia_Location.objects.get(Location_name=pk_or_name)
        except Kenindia_Location.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = Location_Serializer(location)
    return Response(serializer.data)
def Userall_view(request):
    Users = CustomUser.objects.all()
    serializer =  UserallSerializer(Users, many = True)
    return JsonResponse({"Users":serializer.data})
@api_view(['GET'])
def User_detail(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserallSerializer(user)
    return Response(serializer.data)
# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         'api/token',
#         'api/token/refresh',
#     ]
#     return Response(routes)
