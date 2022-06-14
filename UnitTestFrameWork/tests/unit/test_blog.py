from unittest import TestCase
from UnitTestFrameWork.blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        blog = Blog('Test', 'Test Author')

        self.assertEqual('Test', blog.title)
        self.assertEqual('Test Author', blog.author)
        self.assertListEqual([], blog.posts)

    def test_repr(self):
        blog = Blog('Test', 'Test Author')
        blog2 = Blog('My Day', 'Rolf')

        self.assertEqual(blog.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(blog2.__repr__(), 'My Day by Rolf (0 posts)')

    def test_repr_multiple_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.posts = ['test']
        blog2 = Blog('My Day', 'Rolf')
        blog2.posts = ['test', 'another']

        self.assertEqual(blog.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(blog2.__repr__(), 'My Day by Rolf (2 posts)')
