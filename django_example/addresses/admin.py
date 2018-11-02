from django.contrib import admin
from django.contrib.admin import register
from .models import Address


@register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass
