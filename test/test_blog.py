import unittest
import src.blog
from unittest import TestCase
from unittest.mock import patch

class TestBlog(TestCase):
    def setUp(self):
        self.name = "Test_user"
    def tearDown(self):
        self.name = None

    @patch("src.blog.Blog")
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()
        blog.posts.return_value = [
            {
                "userID": 1,
                "id": 1,
                "title": "test case",
                "body": "Far out in the uncharted backwaters of the unfashionable ..."
            }
        ]
        response = blog.posts()
        self.assertIsNotNone(response) # The mock response is not null.
        self.assertIsInstance(response[0], dict) # The mock response instance type is dict
        assert MockBlog is src.blog.Blog  # The mock is equivalent to the original
        assert MockBlog.called  # The mock wasP called


if __name__ == '__main__':
    unittest.main()