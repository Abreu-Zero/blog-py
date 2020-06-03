blogs_data = {}


def main_menu():
    print_blogs()


def print_blogs():
    for key, value in blogs_data.items():
        print()
        print("- {}".format(value))
