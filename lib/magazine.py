class Magazine:
    def __init__(self, title, category, id=None):
        self.id = id
        self.title = title
        self.category = category

    def articles(self):
        from lib.db import CURSOR
        CURSOR.execute("SELECT * FROM articles WHERE magazine_id = ?", (self.id,))
        from .article import Article
        return [Article(row[1], None, self, row[0]) for row in CURSOR.fetchall()]

    def contributors(self):
        from lib.db import CURSOR
        CURSOR.execute("""
            SELECT DISTINCT authors.id, authors.name FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
        """, (self.id,))
        from .author import Author
        return [Author(row[1], row[0]) for row in CURSOR.fetchall()]
