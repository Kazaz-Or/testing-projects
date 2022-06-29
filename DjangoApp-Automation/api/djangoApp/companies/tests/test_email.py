import json

from unittest.mock import patch
from django.core import mail


def test_send_email(settings, mailoutbox):
        settings.EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend"
        assert len(mailoutbox) == 0
        mail.send_mail(subject="Test Subject",
                       message="Test Message",
                       from_email="testmail@dev.io",
                       recipient_list=["testmail2@dev.io"],
                       fail_silently=False)
        assert len(mailoutbox) == 1
        assert mailoutbox[0].subject == "Test Subject"


def test_send_email_without_arguments(client):
    with patch("api.djangoApp.companies.views.send_mail") as mocked_send_mail_function:
        response = client.post(path='/send-email')
        response_content = json.loads(response.content)

        assert response.status_code == 200
        assert response_content['status'] == 'success'
        assert response_content['info'] == 'email sent successfully'

        mocked_send_mail_function.assert_called_with(subject=None,
                                                     message=None,
                                                     from_email="kazi@dev.io",
                                                     recipient_list=['kazi@dev.io'])


def test_send_email_with_get_method(client):
    response = client.get(path='/send-email')

    assert response.status_code == 405
    assert json.loads(response.content) == {"detail": 'Method "GET" not allowed.'}
