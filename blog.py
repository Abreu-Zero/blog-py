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

