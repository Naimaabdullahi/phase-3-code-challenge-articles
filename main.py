from lib.db import CURSOR, CONN
from lib.author import Author
from lib.article import Article
from lib.magazine import Magazine

def main():
    # Contributors to Tech Weekly
    print("== Contributors to Tech Weekly ==")
    CURSOR.execute("SELECT id FROM magazines WHERE title = 'Tech Weekly'")
    result = CURSOR.fetchone()
    if result:
        magazine_id = result[0]
        mag = Magazine("Tech Weekly", "Technology", magazine_id)
        for author in mag.contributors():
            print(author.name)

    # All article titles
    print("== Article Titles ==")
    for article in Article.all():
        print(article[1])  # title column

if __name__ == "__main__":
    main()
