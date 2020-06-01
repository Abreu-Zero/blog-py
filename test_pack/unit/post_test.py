from unittest import TestCase
from post import Post


class PostTest(TestCase):

    def test_create_post(self):
        new_post = Post("Test Post", "Test Content")

        self.assertEqual("Test Post", new_post.title)
        self.assertEqual("Test Content", new_post.content)

    def test_json(self):
        new_post = Post("Test Post", "Test Content")
        expected = {"title": "Test Post", "content": "Test Content"}

        self.assertDictEqual(expected, new_post.json())
        