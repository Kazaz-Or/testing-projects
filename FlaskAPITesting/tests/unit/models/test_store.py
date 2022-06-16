from FlaskAPITesting.models.store import StoreModel
from FlaskAPITesting.tests.basetest import BaseTest


class StoreTest(BaseTest):
    def test_create_store(self):
        store = StoreModel('test-store')

        self.assertEqual(store.name, 'test-store')
