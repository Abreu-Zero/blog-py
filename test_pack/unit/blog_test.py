from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        new_blog = Blog("Test", "Test Author")

        self.assertEqual("Test", new_blog.title)
        self.assertEqual("Test Author", new_blog.author)
        self.assertEqual(len([]), len(new_blog.posts))
        self.assertListEqual([], new_blog.posts)

    def test_repr(self):
        new_blog = Blog("My Test Blog", "Amazing Anonym Author")
        self.assertEqual(new_blog.__repr__(), "My Test Blog by Amazing Anonym Author - 0 Posts")
        new_blog.posts = ["This is a test Post"]
        self.assertEqual(new_blog.__repr__(), "My Test Blog by Amazing Anonym Author - 1 Post")
        new_blog.posts = ["This is a test Post", "This is another test post"]
        self.assertEqual(new_blog.__repr__(), "My Test Blog by Amazing Anonym Author - 2 Posts")
