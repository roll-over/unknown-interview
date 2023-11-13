import requests
import os

PUBLIC_EXTERNAL_URL = os.environ["PUBLIC_EXTERNAL_URL"]


def test_ping_pong():
    ping = requests.get(f"{PUBLIC_EXTERNAL_URL}/api/ping")
    assert ping.status_code == 200
    assert ping.json() == "pong"
