import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")
    return "pass"


@pytest.fixture(scope="function")
def secondWork():
    print("I setup function instance")
    yield
    print("teardown validation")


@pytest.mark.smoke  # marking as a smoke test
def test_inicialCheck(preWork):
    print("first test")
    assert preWork == "pass"


@pytest.mark.skip  # skips the test
def test_secondCheck(preWork, secondWork):
    print("second test")
