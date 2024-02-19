from django.urls import path
from .views import CustomUserCreateView, LoginView,RefreshTokenView

urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', RefreshTokenView.as_view(), name='refresh-token'),
]
