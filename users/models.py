from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# from django.db import models
# from master.Models.dealership import Dealership


class CustomUser(AbstractUser):
    Address = models.CharField(max_length=100, null=True)
    City = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'auth_user'
