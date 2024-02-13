from django.db import models

class Printer(models.Model):
    Printer_name = models.CharField(max_length = 500)
    time_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Printer_name
class Toner(models.Model):
    Toner_name = models.CharField(max_length = 500,default = "")
    printer_name = models.ForeignKey(Printer, null = True ,on_delete = models.SET_NULL)
    quantity = models.PositiveIntegerField(default = 0)
    time_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Toner_name
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
    Staff_ID = models.CharField(max_length = 500 , default = "", unique = True)
    Department = models.CharField(max_length = 500 , default = "")
    Location = models.CharField(max_length = 500 , default = "")
    toner = models.ForeignKey(Toner, null=True, on_delete=models.SET_NULL)
    printer_name = models.CharField(max_length = 500 , default = "")
    issued = models.BooleanField(default = False)
    Date_of_request = models.DateTimeField(auto_now_add = True)
    _previous_issued = models.BooleanField(default=False, editable=False)


    def __str__(self):
        return self.Staff_name
