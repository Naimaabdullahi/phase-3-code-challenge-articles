import sqlite3

conn = sqlite3.connect('articles.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM articles")
cursor.execute("DELETE FROM authors")
cursor.execute("DELETE FROM magazines")

# Insert Authors
cursor.execute("INSERT INTO authors (name) VALUES ('Alice')")
cursor.execute("INSERT INTO authors (name) VALUES ('Bob')")

# Insert Magazines
cursor.execute("INSERT INTO magazines (title, category) VALUES ('Tech Weekly', 'Technology')")
cursor.execute("INSERT INTO magazines (title, category) VALUES ('Health Monthly', 'Health')")

# Insert Articles
cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('AI in 2025', 1, 1)")
cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Python Tricks', 1, 1)")
cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Healthy Eating', 2, 2)")

conn.commit()
conn.close()
