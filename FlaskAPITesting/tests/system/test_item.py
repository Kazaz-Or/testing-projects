import json

from FlaskAPITesting.models.user import UserModel
from FlaskAPITesting.models.item import ItemModel
from FlaskAPITesting.models.store import StoreModel
from FlaskAPITesting.tests.basetest import BaseTest


class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp()
        with self.app as client:
            with self.app_context:
                UserModel('test', '1234').save_to_db()
                auth_request = client.post('/auth', data=json.dumps({
                    'username': 'test',
                    'password': '1234'
                }), headers={'Content-Type': 'application/json'})
                self.auth_header = "JWT {}".format(json.loads(auth_request.data)['access_token'])

    def test_item_no_auth(self):
        with self.app as client:
            response = client.get('/item/test')
            self.assertEqual(response.status_code, 401)

    def test_item_not_found(self):
        with self.app as client:
            response = client.get('/item/test', headers={'Authorization': self.auth_header})
            self.assertEqual(response.status_code, 404)

    def test_item_found(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                ItemModel('test', 17.99, 1).save_to_db()
                response = client.get('/item/test', headers={'Authorization': self.auth_header})

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(d1={'name': 'test', 'price': 17.99},
                                     d2=json.loads(response.data))

    def test_delete_item(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                ItemModel('test', 17.99, 1).save_to_db()
                response = client.delete('/item/test', headers={'Authorization': self.auth_header})

                self.assertEqual(response.status_code, 200)
                self.assertDictEqual(d1={'message': 'Item deleted'},
                                     d2=json.loads(response.data))

    def test_create_item(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                response = client.post('/item/test', data={'price': 17.99, 'store_id': 1})

                self.assertEqual(response.status_code, 201)
                self.assertEqual(ItemModel.find_by_name('test').price, 17.99)
                self.assertDictEqual(d1={'name': 'test', 'price': 17.99},
                                     d2=json.loads(response.data))

    def test_create_duplicate_item(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                client.post('/item/test', data={'price': 17.99, 'store_id': 1})
                response = client.post('/item/test', data={'price': 17.99, 'store_id': 1})

                self.assertEqual(response.status_code, 400)

    def test_put_item(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                response = client.put('/item/test', data={'price': 17.99, 'store_id': 1}, headers={'Authorization': self.auth_header})

                self.assertEqual(response.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('test').price, 17.99)
                self.assertDictEqual(d1={'name': 'test', 'price': 17.99},
                                     d2=json.loads(response.data))

    def test_put_update_item(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                client.put('/item/test', data={'price': 17.99, 'store_id': 1})
                response = client.put('/item/test', data={'price': 18.99, 'store_id': 1}, headers={'Authorization': self.auth_header})

                self.assertEqual(response.status_code, 200)
                self.assertEqual(ItemModel.find_by_name('test').price, 18.99)

    def test_item_list(self):
        with self.app as client:
            with self.app_context:
                StoreModel('test').save_to_db()
                ItemModel('test', 17.99, 1).save_to_db()
                response = client.get('/items')

                self.assertDictEqual(d1={'items': [{'name': 'test', 'price': 17.99}]},
                                     d2=json.loads(response.data))
