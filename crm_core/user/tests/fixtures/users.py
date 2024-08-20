import pytest
from model_bakery import baker

from crm_core.user.models import User

pytestmark = pytest.mark.django_db


@pytest.fixture
def staff_user():
    return baker.make(User, is_staff=True)


@pytest.fixture
def regular_user():
    return baker.make(User, is_staff=False)
