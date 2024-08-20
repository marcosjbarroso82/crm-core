import os

import pytest
from rest_framework.test import APIClient

# Set on the earliest possible moment
os.environ['PYTEST_RUNNING'] = 'true'


@pytest.fixture
def api_client():
    return APIClient()


from crm_core.customer.tests.fixtures import *  # noqa
from crm_core.user.tests.fixtures import *  # noqa
