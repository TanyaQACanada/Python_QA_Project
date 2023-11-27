import pytest
import requests
# from tests.api.api_client import SimpleClient

class SimpleClient:
    def __init__(self):
        self.session = requests.session()

    def get(self, endpoint):
        return self.session.get(f"{'https://jsonplaceholder.typicode.com'}{endpoint}")

    def post(self, endpoint, data):
        return self.session.post(f"{'https://jsonplaceholder.typicode.com'}{endpoint}", data)


@pytest.fixture()
def simple_client():
    client = SimpleClient()
    yield client
    client.session.close()

@pytest.fixture(autouse=True)
def fine_text():
    print('Sending request...')

