import pytest
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
def test_regular_user_cannot_access_users_endpoint(regular_user, api_client):
    # Generate a JWT token for the regular_user
    refresh = RefreshToken.for_user(regular_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    response = api_client.get('/api/v1/users/', headers=headers)
    assert response.status_code == 403


@pytest.mark.django_db
def test_staff_user_can_access_users_endpoint(staff_user, api_client):
    # Generate a JWT token for the staff_user
    refresh = RefreshToken.for_user(staff_user)
    access_token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {access_token}'}

    response = api_client.get('/api/v1/users/', headers=headers)
    assert response.status_code == 200
