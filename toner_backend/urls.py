"""
URL configuration for toner_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from toner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('toner_requests/',views.Toner_requests),
    path('toners/',views.Toners_view),
    path('printers/',views.Printer_view),
    path('departments/',views.Department_view),
    path('locations/',views.Location_view)
]
