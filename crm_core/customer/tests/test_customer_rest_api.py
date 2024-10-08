import shutil
import tempfile

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from rest_framework_simplejwt.tokens import RefreshToken

from crm_core.customer.models import Customer
from crm_core.customer.tests.fixtures.customers import customer, customer_photo, customer_with_photo

# Constants
PHOTO_FILENAME = 'test_photo.jpg'
PHOTO_CONTENT = b'test photo content'
PHOTO_CONTENT_TYPE = 'image/jpeg'


@pytest.fixture(scope='function')
def temp_media_root():
    temp_dir = tempfile.mkdtemp()
    with override_settings(MEDIA_ROOT=temp_dir):
        yield temp_dir
    shutil.rmtree(temp_dir)


@pytest.mark.django_db
@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
def test_staff_user_can_add_photo_to_customer_without_photo(staff_user, api_client, customer, temp_media_root):
    """
    Test that a staff user can add a photo to a customer without a photo.
    """
    # Generate a JWT token for the staff_user
    refresh = RefreshToken.for_user(staff_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    # Create a SimpleUploadedFile instance
    photo = SimpleUploadedFile(PHOTO_FILENAME, PHOTO_CONTENT, content_type=PHOTO_CONTENT_TYPE)

    # Perform the API request to add the photo to the customer
    url = f'/api/v1/customers/{customer.uuid}/photo/'
    response = api_client.post(url, {'photo': photo}, format='multipart', headers=headers)

    # Assert the response status code
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"

    # Refresh the customer instance and assert the photo was added
    customer.refresh_from_db()
    assert customer.photo, "Customer photo was not added"


@pytest.mark.django_db
@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
def test_staff_user_can_update_customer_photo(staff_user, api_client, customer_with_photo, temp_media_root):
    # Generate a JWT token for the staff_user
    refresh = RefreshToken.for_user(staff_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    # Create a new mock photo file
    new_photo = SimpleUploadedFile("new_photo.jpg", b"new_file_content", content_type="image/jpeg")

    # Make a PUT request to update the customer's photo
    response = api_client.post(
        f'/api/v1/customers/{customer_with_photo.uuid}/photo/', headers=headers, data={'photo': new_photo}
    )

    # Check the response status code
    assert response.status_code == 201


@pytest.mark.django_db
@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
def test_staff_user_can_delete_customer_photo(staff_user, api_client, customer_with_photo, temp_media_root):
    # Generate a JWT token for the staff_user
    refresh = RefreshToken.for_user(staff_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    # Make a DELETE request to remove the customer's photo
    response = api_client.delete(f'/api/v1/customers/{customer_with_photo.uuid}/photo/', headers=headers)

    # Check the response status code
    assert response.status_code == 204

    # Verify that the photo was removed from the customer
    customer_with_photo.refresh_from_db()
    with pytest.raises(Customer.photo.RelatedObjectDoesNotExist):
        _ = customer_with_photo.photo
