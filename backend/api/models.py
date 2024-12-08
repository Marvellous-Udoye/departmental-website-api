from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    department = models.CharField(max_length=500)
    matricno = models.CharField(max_length=100, unique=True)
    phonenumber = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username