from django.urls import path
from . import views

urlpatterns = [
    path('toner_requests/', views.Toner_requests, name='toner_requests'),
    path('toner_requests/<int:pk>/', views.Toner_request_detail, name='toner_request_detail'),
    path('toners/', views.Toners_view, name='toners'),
    path('toners/<int:pk>/', views.Toner_detail, name='toner_detail'),
    path('printers/', views.Printer_view, name='printers'),
    path('printers/<int:pk>/', views.Printer_detail, name='printer_detail'),
    path('departments/', views.Department_view, name='departments'),
    path('departments/<str:pk_or_name>/', views.Department_detail, name='department_detail'),
    path('locations/', views.Location_view, name='locations'),
    path('locations/<str:pk_or_name>/', views.Location_detail, name='location_detail'),
    path('users/', views.Userall_view, name='users'),
    path('users/<int:pk>/', views.User_detail, name='user_detail'),
    # path('routes/', views.getRoutes, name='get_routes'),
]
