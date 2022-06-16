from FlaskAPITesting.models.store import StoreModel
from FlaskAPITesting.models.item import ItemModel
from FlaskAPITesting.tests.basetest import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test-store')

        self.assertListEqual(store.items.all(), [])

    def test_crud(self):
        with self.app_context:
            store = StoreModel('test-store')

            self.assertIsNone(StoreModel.find_by_name('test-store'))
            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test-store'))
            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test-store'))

    def test_store_relationship(self):
        with self.app_context:
            store = StoreModel('test-store')
            item = ItemModel('test-item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test-item')

    def test_store_json(self):
        with self.app_context:
            store = StoreModel('test-store')
            item = ItemModel('test-item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()
            expected = {
                'name': 'test-store',
                'items': [{'name': 'test-item', 'price': 19.99}],
            }

            self.assertDictEqual(store.json(), expected)


