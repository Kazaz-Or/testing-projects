from unittest import TestCase
from UnitTestFrameWork.post import Post


class PostTest(TestCase):
    def test_create_post(self):
        post = Post('Test', 'Test Content')
        self.assertEqual('Test', post.title)
        self.assertEqual('Test Content', post.content)

    def test_compare_json(self):
        post = Post ('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}

        self.assertDictEqual(expected, post.json())
