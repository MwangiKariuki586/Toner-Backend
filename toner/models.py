from django.db import models

class Printer(models.Model):
    Printer_name = models.CharField(max_length = 500)
    time_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Printer_name
class Toner(models.Model):
    Toner = models.CharField(max_length = 500,default = "")
    printer_name = models.ForeignKey(Printer, null = True ,on_delete = models.SET_NULL)
    time_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Toner
class Kenindia_Department(models.Model):
    Department_name = models.CharField(max_length = 500)
    time_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Department_name
class Kenindia_Location(models.Model):
    Location_name = models.CharField(max_length = 500)
    time_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Location_name
class Toner_Request(models.Model):
    Staff_name = models.CharField(max_length = 500)
    Staff_ID = models.CharField(max_length = 500 , default = "")
    Department = models.ForeignKey(Kenindia_Department,null = True ,on_delete = models.SET_NULL)
    Location = models.ForeignKey(Kenindia_Location,null = True ,on_delete = models.SET_NULL)
    Toner_name = models.ForeignKey(Toner,null = True ,on_delete = models.SET_NULL)
    printer_name = models.ForeignKey(Printer,null = True ,on_delete = models.SET_NULL)
    issued = models.BooleanField(default = False)
    Date_of_request = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.Staff_name
