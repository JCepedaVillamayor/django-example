import pytest
from ..models import Address
from .factories import AddressFactory, UserFactory

from django.db import IntegrityError


class TestModelAddress:
    def test_model_creation_success(self):
        assert Address.objects.count() == 0
        sample_address = AddressFactory()
        assert sample_address is not None
        assert Address.objects.count() == 1

    @pytest.mark.parametrize("attr", ["address", "city", "state", "zipcode", "user"])
    def test_model_attr_not_null_when_saving(self, attr):
        fake_user = UserFactory()
        sample_address = AddressFactory.build()
        sample_address.user = fake_user
        # save user model first
        setattr(sample_address, attr, None)
        with pytest.raises(IntegrityError):
            sample_address.save()
