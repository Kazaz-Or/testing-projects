from RestAPIAutomationFW.config import APP_URL, SESSION, LOG


def test_health():
    LOG.info("test_health")
    response = SESSION.get(f"{APP_URL}/health")
    assert response.status_code == 200

