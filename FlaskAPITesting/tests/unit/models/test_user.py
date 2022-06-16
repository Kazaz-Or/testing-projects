from FlaskAPITesting.models.user import UserModel
from FlaskAPITesting.tests.basetest import BaseTest


class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abcd')

        self.assertEqual(user.username, 'test')
        self.assertEqual(user.password, 'abcd')