from django.urls import path
from toner import views

urlpatterns = [
    path('toner_requests/',views.Toner_requests),
    path('toners/',views.Toners_view),
    path('printers/',views.Printer_view),
    path('departments/',views.Department_view),
    path('locations/',views.Location_view),

]