from django.http import JsonResponse
from django.shortcuts import render
from .models import Toner_Request
from .serializers import Toner_RequestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status

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
