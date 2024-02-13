# custom_users/models.py
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from toner.models import Kenindia_Department,Kenindia_Location

class CustomUserManager(BaseUserManager):
    def create_user(self, staff_id, password=None, **extra_fields):
        if not staff_id:
            raise ValueError('The Email field must be set')
        staff_id = self.normalize_email(staff_id)
        user = self.model(staff_id=staff_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, staff_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(staff_id, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    staff_id = models.CharField(unique=True,max_length=3)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    department = models.ForeignKey(Kenindia_Department,null = True ,on_delete = models.SET_NULL )
    location = models.ForeignKey(Kenindia_Location,null = True ,on_delete = models.SET_NULL)
    Date_created = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'staff_id'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name
