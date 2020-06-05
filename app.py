import blog
import post

blogs_data = dict()
MENU_PROMPT = "Press 'c' for create, 'l' to list, 'r' to read, 'p' to post and 'q' to quit: "


def main_menu():
    print_blogs()
    selection = input(MENU_PROMPT)

    while selection != "q":
        if selection == "c":
            create_blog()

        elif selection == "p":
            create_post()

        elif selection == "r":
            read_blog()

        elif selection == "l":
            print_blogs()

        selection = input(MENU_PROMPT)


def print_blogs():
    for key, value in blogs_data.items():
        print()
        print("- {}".format(value))


def create_blog():
    blog_title = input("Please insert your blog's title: ")
    blog_author = input("Now please insert your pseudonym: ")

    new_blog = blog.Blog(blog_title, blog_author)
    blogs_data[blog_title] = new_blog


def create_post():
    post_title = input("Please insert your post's title: ")
    post_content = input("Now write the post, press enter to submit: ")
    blog_to_post = input("Where should we post this? ")

    for key in blogs_data:
        if blog_to_post == key:
            blog_to_post = blogs_data[key]
            blog_to_post.create_new_post(post_title, post_content)
            break

        raise (Exception, "blog not found")


def read_blog():
    blog_to_read = input("Select a blog to read: ")

    for key in blogs_data:
        if blog_to_read == key:
            blog_to_read = blogs_data[key]
            print_posts(blog_to_read)
            break
        raise (Exception, "blog not found")


def print_posts(blog):
    for item in blog.posts:
        print_post(item)


def print_post(post):
    print('''
    --------------------------
    -{}
    --------------------------
    
    {}
    '''.format(post.title, post.content))
