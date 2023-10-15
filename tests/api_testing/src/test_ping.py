import requests
import os

EXTERNAL_URL = os.environ["EXTERNAL_URL"]


def test_ping_pong():
    ping = requests.get(f"{EXTERNAL_URL}/api/ping")
    assert ping.status_code == 200
    assert ping.json() == "pong"
