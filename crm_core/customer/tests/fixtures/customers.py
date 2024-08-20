import pytest
from model_bakery import baker

from crm_core.customer.models import Customer, CustomerPhoto

pytestmark = pytest.mark.django_db

@pytest.fixture
def customer():
    return baker.make(Customer)

@pytest.fixture
def customer_photo():
    return baker.make(CustomerPhoto)

@pytest.fixture
def customer_with_photo(customer, customer_photo):
    customer_photo.customer = customer
    customer_photo.save()
    return customer
