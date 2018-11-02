from django.contrib.auth.models import User
import factory
from factory.django import DjangoModelFactory

from ..models import Address


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    password = "foobarfoobar"


class AddressFactory(DjangoModelFactory):
    class Meta:
        model = Address

    user = factory.SubFactory(UserFactory)
    address = factory.Faker("address")
    city = factory.Faker("city")
    state = factory.Faker("state")
    zipcode = factory.Faker("zipcode")
