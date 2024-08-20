import pytest
from rest_framework_simplejwt.tokens import RefreshToken

from crm_core.customer.tests.fixtures.customers import customer, customer_photo, customer_with_photo

from crm_core.user.tests.fixtures.users import staff_user, regular_user
from crm_core.customer.models import Customer


@pytest.mark.django_db
def test_customer_with_photo_has_photo(customer_with_photo):
    assert customer_with_photo.photo is not None


@pytest.mark.django_db
def test_customer_without_photo_has_no_photo(customer):
    # assert customer.photo is None
    with pytest.raises(Customer.photo.RelatedObjectDoesNotExist):
        _ = customer.photo


@pytest.mark.django_db
def test_regular_user_cannot_access_customers_endpoint(regular_user, api_client):
    # Generate a JWT token for the regular_user
    refresh = RefreshToken.for_user(regular_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    response = api_client.get('/api/v1/customers/', headers=headers)
    assert response.status_code == 403


@pytest.mark.django_db
def test_staff_user_can_access_customers_endpoint(staff_user, api_client):
    # Generate a JWT token for the staff_user
    refresh = RefreshToken.for_user(staff_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    response = api_client.get('/api/v1/customers/', headers=headers)
    assert response.status_code == 200


@pytest.mark.django_db
def test_regular_user_cannot_access_customer_detail_endpoint(regular_user, api_client, customer):
    # Generate a JWT token for the regular_user
    refresh = RefreshToken.for_user(regular_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    response = api_client.get(f'/api/v1/customers/{customer.uuid}/', headers=headers)

    assert response.status_code == 403


@pytest.mark.django_db
def test_staff_user_can_access_customer_detail_endpoint(staff_user, api_client, customer):
    # Generate a JWT token for the staff_user
    refresh = RefreshToken.for_user(staff_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    response = api_client.get(f'/api/v1/customers/{customer.uuid}/', headers=headers)

    assert response.status_code == 200

