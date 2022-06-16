import itertools
import json

from FlaskAPITesting.models.user import UserModel
from FlaskAPITesting.tests.basetest import BaseTest


class UserTest(BaseTest):
    def test_register_user(self):
        with self.app as client:
            with self.app_context:
                response = client.post('/register', data={'username': 'test', 'password': 'abcd'})

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message': 'User created successfully'}, json.loads(response.data))

    def test_register_and_login(self):
        with self.app as client:
            with self.app_context:
                client.post('/register', data={'username': 'test', 'password': 'abcd'})
                auth_response = client.post('/auth',
                                           data=json.dumps({'username': 'test', 'password': 'abcd'}),
                                           headers={'Content-Type': 'application/json'})

                self.assertIn('access_token', json.loads(auth_response.data).keys())

    def test_register_duplicate_user(self):
        for _ in itertools.repeat(None, 2):
            with self.app as client:
                with self.app_context:
                    response = client.post('/register', data={'username': 'test', 'password': 'abcd'})

        self.assertEqual(response.status_code, 400)
        self.assertDictEqual({'message': 'A user with this username already exists'}, json.loads(response.data))

