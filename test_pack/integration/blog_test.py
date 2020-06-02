from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

    @staticmethod
    def create_test_blog():
        new_blog = Blog("My Test Blog", "Amazing Anonym Author")
        new_blog.create_new_post("First Post", "Some awesome content")
        return new_blog

    def test_create_new_post(self):

        new_blog = self.create_test_blog()
        self.assertEqual(len(new_blog.posts), 1)

        test_post = new_blog.posts[0]
        self.assertEqual(test_post.title, "First Post")
        self.assertEqual(test_post.content, "Some awesome content")

    def test_json(self):
        new_blog = self.create_test_blog()

        expected_posts_json = {"title": "First Post", "content": "Some awesome content"}
        expected_blog_json = {"title": "My Test Blog",
                              "author": "Amazing Anonym Author",
                              "posts": [expected_posts_json]}

        self.assertDictEqual(new_blog.json(), expected_blog_json)


