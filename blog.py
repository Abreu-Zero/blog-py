from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        plural = ""
        if len(self.posts) != 1:
            plural = "s"

        return self.title + " by " + self.author + " - " + str(len(self.posts)) + " Post" + plural

    def create_new_post(self, title, content):
        new_post = Post(title, content)
        self.posts.append(new_post)

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts]
        }