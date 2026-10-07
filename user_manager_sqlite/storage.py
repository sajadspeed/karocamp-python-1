import sqlite3


DATABASE = "users.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            is_verified INTEGER NOT NULL,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            city TEXT NOT NULL,
            skills TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()
