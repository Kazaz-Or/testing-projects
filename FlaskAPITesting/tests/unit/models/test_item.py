from FlaskAPITesting.tests.basetest import BaseTest
from FlaskAPITesting.models.item import ItemModel


class ItemTest(BaseTest):
    def test_create_item(self):
        item = ItemModel('test', 19.99, 1)

        self.assertEqual(item.name, 'test')
        self.assertEqual(item.price, 19.99)
        self.assertEqual(item.store_id, 1)
        self.assertIsNone(item.store)

    def test_item_json(self):
        item = ItemModel('test', 19.99, 1)
        expected = {'name': 'test', 'price': 19.99}

        self.assertEqual(item.json(), expected)
