from django.db import models

from management.models import Resident


class AppUser(models.Model):
    name = models.CharField(max_length=20)
    resident = models.OneToOneField(Resident)
    identity = models.CharField(max_length=18)
    mobile = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
