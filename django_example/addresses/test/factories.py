from django.contrib.auth.models import User
import factory
from factory.django import DjangoModelFactory

from ..models import Address


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User


class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address

    user = factory.SubFactory(UserFactory)
