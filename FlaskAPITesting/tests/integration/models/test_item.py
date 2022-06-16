from FlaskAPITesting.models.item import ItemModel
from FlaskAPITesting.tests.basetest import BaseTest
from FlaskAPITesting.models.store import StoreModel


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context:
            StoreModel('test-store').save_to_db()
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'))
            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))
            item.delete_from_db()

    def test_store_relationship(self):
        with self.app_context:
            store = StoreModel('test-store')
            item = ItemModel('test', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test-store')
