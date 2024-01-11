from django.http import JsonResponse
from django.shortcuts import render
from .models import Toner_Request
from .serializers import Toner_RequestSerializer

def Toner_requests(request):
    requests_toners = Toner_Request.objects.all()
    serializer =  Toner_RequestSerializer(requests_toners, many = True)
    return JsonResponse({"Toner_requests":serializer.data},safe=False)
