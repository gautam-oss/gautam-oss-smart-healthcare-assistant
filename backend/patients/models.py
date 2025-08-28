from django.db import models
from django.contrib.auth.models import AbstractUser

class Patient(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='patient_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='patient',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='patient_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='patient',
    )

    def __str__(self):
        return self.username