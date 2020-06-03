from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):

    def test_print_blogs(self):

        blog = Blog("My Test Blog", "Amazing Anonym Author")
        app.blogs_data = {"Test": blog}

        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with("- My Test Blog by Amazing Anonym Author - 0 Posts")
