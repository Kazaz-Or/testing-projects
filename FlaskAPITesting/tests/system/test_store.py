import json

from FlaskAPITesting.models.store import StoreModel
from FlaskAPITesting.tests.basetest import BaseTest
from FlaskAPITesting.models.item import ItemModel


class StoreTest(BaseTest):
    def test_store_not_found(self):
        with self.app as client:
            response = client.get('/store/test')
            self.assertEqual(response.status_code, 404)

    def test_store_found(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                response = client.get('/store/test')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(d1={'name': 'test', 'items': []},
                                     d2=json.loads(response.data))

    def test_store_with_items_found(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                ItemModel('test', 2.99, 1).save_to_db()
                response = client.get('/store/test')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(d1={'name': 'test', 'items': [{'name': 'test', 'price': 2.99}]},
                                     d2=json.loads(response.data))

    def test_delete_store(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                response = client.delete('/store/test')

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(d1={'message': 'Store deleted'},
                                     d2=json.loads(response.data))

    def test_create_store(self):
        with self.app as client:
            with self.app_context:
                response = client.post('/store/test')

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertDictEqual(d1={'name': 'test', 'items': []},
                                     d2=json.loads(response.data))

    def test_create_duplicate_store(self):
        with self.app as client:
            with self.app_context:
                client.post('/store/test')
                response = client.post('/store/test')

                self.assertEqual(response.status_code, 400)

    def test_store_list(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                response = client.get('/stores')

                self.assertDictEqual(d1={'stores': [{'name': 'test', 'items': []}]},
                                     d2=json.loads(response.data))

    def test_store_with_items_list(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                ItemModel('test', 17.99, 1).save_to_db()
                response = client.get('/stores')

                self.assertDictEqual(d1={'stores': [{'name': 'test', 'items': [{'name': 'test', 'price': 17.99}]}]},
                                     d2=json.loads(response.data))
