from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        new_blog = Blog("Test", "Test Author")

        self.assertEqual("Test", new_blog.title)
        self.assertEqual("Test Author", new_blog.author)
        self.assertEqual(len([]), len(new_blog.posts))
        self.assertListEqual([], new_blog.posts)