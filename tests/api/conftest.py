import pytest
from endpoints.placeholder_service import PlaceholderService

@pytest.fixture
def user_api():
    data = PlaceholderService()
    return data