from django.db import models
from django.contrib.auth.models import AbstractUser

class Doctor(AbstractUser):
    specialization = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='doctor_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='doctor',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='doctor_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='doctor',
    )

    def __str__(self):
        return self.username