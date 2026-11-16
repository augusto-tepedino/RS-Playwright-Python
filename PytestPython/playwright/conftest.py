import pytest
from utils.apiBase import APIUtils

@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture
def order_id(playwright, user_credentials):
    email = user_credentials["email"]
    password = user_credentials["password"]
    return APIUtils().createOrder(playwright, email, password)