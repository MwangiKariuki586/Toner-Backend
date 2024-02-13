from django.contrib import admin
from .models import *

class toneradmin(admin.ModelAdmin):
    list_display = ('Staff_name','Staff_ID','Department','Location','toner','printer_name','Date_of_request','issued')
class tonersAdmin(admin.ModelAdmin):
    list_display = ('Toner_name','quantity')

admin.site.register(Toner,tonersAdmin)
admin.site.register(Toner_Request,toneradmin)
admin.site.register(Printer)
admin.site.register(Kenindia_Department)
admin.site.register(Kenindia_Location)
 

