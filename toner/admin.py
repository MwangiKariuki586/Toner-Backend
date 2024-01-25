from django.contrib import admin
from .models import *

class toneradmin(admin.ModelAdmin):
    list_display = ('Staff_name','Staff_ID','Department','Location','Toner_name','printer_name')

admin.site.register(Toner)
admin.site.register(Toner_Request)
admin.site.register(Printer)
admin.site.register(Kenindia_Department)
admin.site.register(Kenindia_Location)
 

