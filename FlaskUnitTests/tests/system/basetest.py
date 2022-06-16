from unittest import TestCase

from FlaskUnitTests.app.app import app


class BaseTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.testing = True
