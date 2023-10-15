import requests
import os

EXTERNAL_URL = os.environ["EXTERNAL_URL"]


def test_get_all_users_list():
    users = requests.get(f"{EXTERNAL_URL}/api/v1/users/")
    assert users.status_code == 200
    assert isinstance(users.json(), list)
    assert len(users.json()) > 0
