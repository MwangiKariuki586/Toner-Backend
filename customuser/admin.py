from django.contrib import admin
from .models import CustomUser

class customUsersAdmin(admin.ModelAdmin):
    list_display = ('staff_id','first_name','last_name','department','location','is_active', 'is_staff','Date_created')
    fieldsets = (
        ('Main Information', {
             'fields': ('staff_id', 'first_name', 'last_name','password'),
         }),
         ('Additional Information', {
             'fields': ('department','location'),
         }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
            }),
     )
admin.site.register(CustomUser,customUsersAdmin)


