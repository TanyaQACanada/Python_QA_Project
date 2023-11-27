import pytest
from pom.api_client import SimpleClient


@pytest.fixture()
def simple_client():
    client = SimpleClient()
    yield client
    client.session.close()

@pytest.fixture(autouse=True)
def fine_text():
    print('Sending request...')

