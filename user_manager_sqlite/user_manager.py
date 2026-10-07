import sqlite3

from storage import get_connection


def find_user(username):
    connection = get_connection()

    user = connection.execute(
        """
        SELECT username, password, is_verified, name, age, city, skills
        FROM users
        WHERE username = ?
        """,
        (username,)
    ).fetchone()

    connection.close()

    if user is None:
        return None

    return row_to_user(user)


def register_user(username, password, name, age, city, skills, is_verified):
    connection = get_connection()

    try:
        connection.execute(
            """
            INSERT INTO users
            (username, password, is_verified, name, age, city, skills)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                username,
                password,
                is_verified,
                name,
                age,
                city,
                ",".join(skills)
            )
        )

        connection.commit()

    except sqlite3.IntegrityError:
        connection.close()
        return False

    connection.close()
    return True


def get_users():
    connection = get_connection()

    rows = connection.execute(
        """
        SELECT username, password, is_verified, name, age, city, skills
        FROM users
        """
    ).fetchall()

    connection.close()

    return [row_to_user(row) for row in rows]


def update_profile(username, name, age, city):
    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE users
        SET name = ?, age = ?, city = ?
        WHERE username = ?
        """,
        (name, age, city, username)
    )

    connection.commit()
    connection.close()

    return cursor.rowcount > 0


def add_skill(username, skill):
    user = find_user(username)

    if user is None:
        return False

    skills = user["skills"]
    skills.append(skill)

    connection = get_connection()

    connection.execute(
        """
        UPDATE users
        SET skills = ?
        WHERE username = ?
        """,
        (",".join(skills), username)
    )

    connection.commit()
    connection.close()

    return True


def change_verification(username):
    user = find_user(username)

    if user is None:
        return False

    connection = get_connection()

    connection.execute(
        """
        UPDATE users
        SET is_verified = ?
        WHERE username = ?
        """,
        (not user["is_verified"], username)
    )

    connection.commit()
    connection.close()

    return True


def delete_user(username):
    connection = get_connection()

    cursor = connection.execute(
        """
        DELETE FROM users
        WHERE username = ?
        """,
        (username,)
    )

    connection.commit()
    connection.close()

    return cursor.rowcount > 0


def row_to_user(row):
    return {
        "username": row["username"],
        "password": row["password"],
        "is_verified": bool(row["is_verified"]),
        "skills": row["skills"].split(",") if row["skills"] else [],
        "profile": {
            "name": row["name"],
            "age": row["age"],
            "city": row["city"]
        }
    }
