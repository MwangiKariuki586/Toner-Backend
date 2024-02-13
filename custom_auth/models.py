from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
from toner.models import Kenindia_Department,Kenindia_Location
class CustomUserManager(BaseUserManager):
    def create_user(self, staffid, password=None, **extra_fields):
        if not staffid:
            raise ValueError('The staffid field must be set')
        user = self.model(staffid=staffid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, staffid, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(staffid, password, **extra_fields)

class CustomUser(AbstractUser):
    email = None
    first_name = None
    last_name = None
    username = None
    staffid = models.CharField(max_length=10, unique=True)
    staff_name = models.CharField(max_length=255)
    department = models.ForeignKey(Kenindia_Department,null = True ,on_delete = models.SET_NULL)
    location = models.ForeignKey(Kenindia_Location,null = True ,on_delete = models.SET_NULL)

    USERNAME_FIELD = 'staffid'
    REQUIRED_FIELDS = ['staff_name','department','location']
    objects = CustomUserManager()
    def __str__(self):
        return self.staffid
