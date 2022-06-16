import json

from FlaskUnitTests.tests.system.basetest import BaseTest


class TestHome(BaseTest):
    def test_home(self):
        with self.app as c:
            response = c.get('/')

            self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        with self.app as c:
            response = c.get('/')

            self.assertEqual(json.loads(response.get_data()), {'message': 'Flask Server!'})
