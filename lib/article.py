class Article:
    def __init__(self, title, author, magazine, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.magazine = magazine

    @classmethod
    def all(cls):
        from lib.db import CURSOR
        CURSOR.execute("SELECT * FROM articles")
        return CURSOR.fetchall()
