import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework_simplejwt.tokens import RefreshToken

from crm_core.customer.tests.fixtures.customers import customer, customer_photo, customer_with_photo

from crm_core.user.tests.fixtures.users import staff_user, regular_user
from crm_core.customer.models import Customer


@pytest.mark.django_db
def test_staff_user_can_add_photo_to_customer_without_photo(staff_user, api_client, customer):
    # Generate a JWT token for the staff_user
    refresh = RefreshToken.for_user(staff_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    # Create a mock photo file
    photo = SimpleUploadedFile("photo.jpg", b"file_content", content_type="image/jpeg")

    # Make a POST request to add a photo to the customer
    response = api_client.post(
        f'/api/v1/customers/{customer.uuid}/photo/',
        headers=headers,
        data={'photo': photo}
    )

    # Check the response status code
    assert response.status_code == 201

    # Verify that the photo was added to the customer
    customer.refresh_from_db()
    assert customer.photo is not None


@pytest.mark.django_db
def test_staff_user_can_update_customer_photo(staff_user, api_client, customer_with_photo):
    # Generate a JWT token for the staff_user
    refresh = RefreshToken.for_user(staff_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    # Create a new mock photo file
    new_photo = SimpleUploadedFile("new_photo.jpg", b"new_file_content", content_type="image/jpeg")

    # Make a PUT request to update the customer's photo
    response = api_client.post(
        f'/api/v1/customers/{customer_with_photo.uuid}/photo/',
        headers=headers,
        data={'photo': new_photo}
    )

    # Check the response status code
    assert response.status_code == 201


@pytest.mark.django_db
def test_staff_user_can_delete_customer_photo(staff_user, api_client, customer_with_photo):
    # Generate a JWT token for the staff_user
    refresh = RefreshToken.for_user(staff_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    # Make a DELETE request to remove the customer's photo
    response = api_client.delete(
        f'/api/v1/customers/{customer_with_photo.uuid}/photo/',
        headers=headers
    )

    # Check the response status code
    assert response.status_code == 204

    # Verify that the photo was removed from the customer
    customer_with_photo.refresh_from_db()
    with pytest.raises(Customer.photo.RelatedObjectDoesNotExist):
        _ = customer_with_photo.photo
