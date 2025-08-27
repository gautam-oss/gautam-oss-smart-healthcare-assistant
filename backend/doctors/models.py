from django.db import models
from django.contrib.auth.models import AbstractUser

class Doctor(AbstractUser):
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username