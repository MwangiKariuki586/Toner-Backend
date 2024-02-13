from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('staffid', 'staff_name', 'department', 'location', 'is_staff', 'last_login')
    fieldsets = (
        (None, {'fields': ('staffid','password')}),
        ('Personal Info', {'fields': ('staff_name', 'department', 'location')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('staffid', 'staff_name', 'department', 'location', 'password1', 'password2'),
        }),
    )
    search_fields = ('staffid', 'staff_name', 'department', 'location')
    ordering = ('staffid',)

# Register the custom user model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)
