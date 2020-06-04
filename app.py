blogs_data = {}
MENU_PROMPT = "Press 'c' for create, 'l' to list, 'r' to read, 'p' to post and 'q' to quit"


def main_menu():
    selection = input(MENU_PROMPT)

    print_blogs()


def print_blogs():
    for key, value in blogs_data.items():
        print()
        print("- {}".format(value))
