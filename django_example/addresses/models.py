from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    additional_info = models.CharField(max_length=128, blank=True)

    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=5)
