from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog


class AppTest(TestCase):

    def test_print_blogs(self):

        blog = Blog("My Test Blog", "Amazing Anonym Author")
        app.blogs_data = {"Test": blog}

        with patch("builtins.print") as mocked_print:   ##patches print to see if blogs are printed
            app.print_blogs()
            mocked_print.assert_called_with("- My Test Blog by Amazing Anonym Author - 0 Posts")

    def test_selection_promt(self):

        with patch("builtins.input") as mocked_input:
            app.main_menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):

        with patch("app.print_blogs") as mocked_print:  ## patches input to check if func called
            with patch("builtins.input"):               ## builtins.input, return_value= to return value
                app.main_menu()
                mocked_print.assert_called()