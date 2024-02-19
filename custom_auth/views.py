from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomUserSerializer, LoginSerializer,RefreshTokenSerializer
from .models import CustomUser

class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        staffid = serializer.validated_data['staffid']
        password = serializer.validated_data['password']
        #check if user exists before authentication
        try:
            user = CustomUser.objects.get(staffid=staffid)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_401_UNAUTHORIZED)
        #.......
        user = CustomUser.objects.get(staffid=staffid)
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
class RefreshTokenView(generics.CreateAPIView):
    serializer_class = RefreshTokenSerializer  # Use the appropriate serializer for refresh token

    def create(self, request, *args, **kwargs):
        refresh = request.data.get('refresh')
        serializer = self.get_serializer(data={'refresh': refresh})

        if serializer.is_valid():
            refresh_token = serializer.validated_data.get('refresh')
            access_token = RefreshToken(refresh_token).access_token

            response_data = {
                'access': str(access_token),
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)