from rest_framework import serializers
from .models import CustomUser
class UserallSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.Department_name', read_only=True)
    location_name = serializers.CharField(source='location.Location_name', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'staff_name', 'staffid','department_name','location_name', 'is_superuser', 'is_active', 'date_joined', 'last_login']
class CustomUserSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['staffid', 'staff_name', 'department', 'location', 'password', 'password_confirmation','is_staff','is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError("Password and password confirmation do not match.")

        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmation', None)  # Remove password_confirmation before saving
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.get('password')
        password_confirmation = validated_data.get('password_confirmation')

        if password and password != password_confirmation:
            raise serializers.ValidationError("Password and password confirmation do not match.")

        # Continue with other updates
        instance.staff_name = validated_data.get('staff_name', instance.staff_name)
        instance.department = validated_data.get('department', instance.department)
        instance.location = validated_data.get('location', instance.location)

        # Update password if provided
        if password:
            instance.set_password(password)

        instance.save()
        return instance
    def delete(self, instance):
        instance.delete()
class LoginSerializer(serializers.Serializer):
    staffid = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)

class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()