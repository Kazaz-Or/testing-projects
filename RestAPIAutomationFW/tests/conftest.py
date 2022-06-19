import pytest
from RestAPIAutomationFW.config import APP_URL, ADMIN_USER, ADMIN_PASSWORD, LOG
from RestAPIAutomationFW.lib.auth import Auth


@pytest.fixture(scope="session")
def login_as_admin():
    LOG.info("login_as_admin")
    response = Auth().login(APP_URL, ADMIN_USER, ADMIN_PASSWORD)
    assert response.status_code == 200

    access_token = response.json()["access_token"]
    yield access_token
