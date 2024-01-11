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
class Toner_Request(models.Model):
    Staff_name = models.CharField(max_length = 500)
    Staff_ID = models.CharField(max_length = 500 , default = "")
    DEPARTMENT_CHOICES = (
    ("IT", "it"),
    ("FINANCE", "Finance"),
    ("ADMIN","Admin"),
    ("PENSION", "Pension"),
    ("INDIVIDUAL LIFE","Individual life"),
    ("LIFE ACCOUNTS", "Life accounts"),
    ("C.O.O","C.O.O"),
    ("G.M","G.M"),
    ("M.D","M.D"),
    ("BRANCH 2","Branch 2"),
    ("BRANCH 1","Branch 1"),
    ("UNDEWRITING HUB","Underwriting Hub"),
    ("HR","HR"),
    ("REINSURANCE","Reinsurance"),
    ("DSF","DSF"),
    ("AUDIT","Audit"),
    ("ACTURIAL","Acturial"),
    ("CLAIMS MOTOR","Claims motor"),
    ("CLAIMS MEDICAL","Claims medical"),
    ("LEGAL","legal"),
    ("CUSTOMER CARE","Customer care"),
)
    Department = models.CharField(max_length=100,
                  choices=DEPARTMENT_CHOICES,
                  default="LIFE ACCOUNTS")
    LOCATION_CHOICES = (
        ("HEAD OFFICE","head office"),
        ("WESTLANDS","westlands"),
        ("ENTERPRISE ROAD","enterprise road"),
        ("NAKURU","nakuru"),
        ("ELDORET","eldoret"),
        ("KISUMU","kisumu"),
        ("MOMBASA","mombasa"),
        ("KISII","kisii"),
        ("NYERI","nyeri"),
        ("THIKA","thika"),
        ("MERU","meru"),
        ("MACHAKOS","machakos"),
    )
    Location = models.CharField(max_length=100,
                  choices=LOCATION_CHOICES,
                  default="HEAD OFFICE")
    Toner_name = models.ForeignKey(Toner, null = True ,on_delete = models.SET_NULL)
    printer_name = models.ForeignKey(Printer, null = True ,on_delete = models.SET_NULL)
    issued = models.BooleanField(default = False)
    Date_of_request = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.Staff_name