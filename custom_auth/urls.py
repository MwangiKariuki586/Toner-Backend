from django.urls import path
from .views import CustomUserCreateView, LoginView

urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]
