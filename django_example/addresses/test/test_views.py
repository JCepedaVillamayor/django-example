import pytest
from django.urls import reverse
from .factories import AddressFactory


class TestPaginationView:
    def create_sample_addresses(self):
        self.addresses = AddressFactory.create_batch(20)

    def test_pagination_success(self, client):
        """
        We request the page normally and we check that
        the status is 200
        """

        self.create_sample_addresses()
        response = client.get(reverse("address_listing"))
        assert response.status_code == 200
        assert len(response.context[-1]["users"]) == 10
        assert response.context[-1]["page_range"] == [1, 2]

    def test_pagination_not_users(self, client):
        """
        Although there are no users in the database,
        we can still render correctly the page

        Args:
            client: the django test client
        """
        response = client.get(reverse("address_listing"))
        assert response.status_code == 200
        assert len(response.context[-1]["users"]) == 0
        assert response.context[-1]["page_range"] == [1]

    def test_pagination_page_size_exceeded(self, client):
        """
        If the page we request is out of bounds,
        we set the page to the last one

        Args:
            client: the django test client
        """
        self.create_sample_addresses()
        response = client.get("{}/?page=50".format(reverse("address_listing")))
        assert response.status_code == 200
        users_pagination = response.context[-1]["users"]
        assert users_pagination.number == users_pagination.paginator.num_pages
        assert len(users_pagination) == 10

    def test_paginator_negative_index(self, client):
        """
        If we set a negative index when requesting the page,
        it should be set to the first one

        Args:
            client: the django test client
        """
        self.create_sample_addresses()
        response = client.get("{}/?page=-1".format(reverse("address_listing")))
        assert response.status_code == 200
        users_pagination = response.context[-1]["users"]
        assert users_pagination.number == 1
        assert len(users_pagination) == 10

    def test_pagination_valuerror(self, client):
        """
        If we do not set the parameter page inside the url,
        the view should catch a valueerror and render the response
        as if the page was the first one

        Args:
            client: the django test client
        """
        self.create_sample_addresses()
        response = client.get("{}/?page=".format(reverse("address_listing")))
        assert response.status_code == 200
        users_pagination = response.context[-1]["users"]
        assert users_pagination.number == 1
        assert len(users_pagination) == 10


class TestPageRangeView:
    def create_sample_addresses(self, amount=70):
        self.addresses = AddressFactory.create_batch(amount)

    @pytest.mark.parametrize("index", [1, 2, 3])
    def test_index_take_lower_pages(self, client, index):
        """
        when the index is lower or equal to 3, the range starts
        at position 0
        """
        self.create_sample_addresses()
        response = client.get("{}/?page={}".format(reverse("address_listing"), index))
        assert response.status_code == 200
        page_range = response.context[-1]["page_range"]
        assert page_range == list(range(1, index + 4))

    @pytest.mark.parametrize("index", [1, 2, 3])
    def test_index_take_upper_pages(self, client, index):
        """
        if the distance between the index and the end of the pagination
        is lower than 3, we take indexes until the last index
        """
        self.create_sample_addresses(30)
        response = client.get("{}/?page={}".format(reverse("address_listing"), index))
        assert response.status_code == 200
        page_range = response.context[-1]["page_range"]
        assert page_range == list(range(1, 4))

    @pytest.mark.parametrize("index", [4, 5, 6, 7])
    def test_index_take_both(self, client, index):
        """
        If the index is in between, we take 6 pages from the range
        """
        self.create_sample_addresses(100)
        response = client.get("{}/?page={}".format(reverse("address_listing"), index))
        assert response.status_code == 200
        page_range = response.context[-1]["page_range"]
        assert len(page_range) == 6

