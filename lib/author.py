from .article import Article

class Author:
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def articles(self):
        from lib.db import CURSOR
        CURSOR.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        rows = CURSOR.fetchall()
        return [Article(row[1], self, None, row[0]) for row in rows]

    def magazines(self):
        from lib.db import CURSOR
        CURSOR.execute(
            "SELECT DISTINCT magazines.id, magazines.title, magazines.category FROM magazines "
            "JOIN articles ON articles.magazine_id = magazines.id "
            "WHERE articles.author_id = ?", (self.id,)
        )
        from .magazine import Magazine
        return [Magazine(row[1], row[2], row[0]) for row in CURSOR.fetchall()]
