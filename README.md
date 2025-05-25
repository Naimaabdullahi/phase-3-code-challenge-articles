Phase 3 Code Challenge - Articles
Project Description
This project models the relationships between Authors, Articles, and Magazines using Python and SQLite without using any ORM. The goal is to practice object-oriented programming, raw SQL queries, and database relationships.

You will find three core models implemented as Python classes:

Author — represents article authors.

Article — represents articles written by authors and published in magazines.

Magazine — represents magazines publishing articles.

The project uses raw SQL to interact with a SQLite database (articles.db) to store and retrieve data.

Project Structure
pgsql
Copy
Edit
phase-3-code-challenge-articles/
├── db/
│   ├── schema.sql         # SQL commands to create tables
│   └── seed.py            # Script to seed initial data into the database
├── lib/
│   ├── __init__.py
│   ├── article.py         # Article class with database methods
│   ├── author.py          # Author class with database methods
│   └── magazine.py        # Magazine class with database methods
├── venv/                  # Python virtual environment (optional)
├── articles.db            # SQLite database file
├── main.py                # Main script to run the program and show outputs
└── README.md              # This README file
Setup Instructions
Create and activate a virtual environment (optional but recommended):

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Create the database tables:

bash
Copy
Edit
sqlite3 articles.db < db/schema.sql
Seed the database with initial data:

bash
Copy
Edit
python3 db/seed.py
Run the main program to test the models:

bash
Copy
Edit
python3 main.py
Database Details
The SQLite database (articles.db) contains three tables:

author: Naima Abdullahi.

The database schema is defined in db/schema.sql. The database is seeded with example data in db/seed.py.

How to Use
The main.py script demonstrates basic usage by:

Listing all contributors to a magazine.

Listing all article titles.

You can extend the models and SQL queries as needed to support more features.

Technologies Used
Python 3

SQLite (via sqlite3 module)

Object-oriented programming

Raw SQL queries (no ORM)

License
This project is open source and free to use.

