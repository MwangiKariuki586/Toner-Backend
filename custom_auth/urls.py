from django.urls import path
from .views import CustomUserCreateView, CustomUserDetailView, CustomUserListView, LoginView,RefreshTokenView

urlpatterns = [
    path('register/', CustomUserCreateView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', RefreshTokenView.as_view(), name='refresh-token'),
    # CRUD operations for users
    path('users/', CustomUserListView.as_view(), name='user-list'),             # List and Create Users
    path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
]
