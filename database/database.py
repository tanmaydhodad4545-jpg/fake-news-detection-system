import sqlite3


DATABASE = "database/news.db"


def create_table():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news TEXT NOT NULL,
            result TEXT NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_prediction(news, result):
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO predictions (news, result)
        VALUES (?, ?)
        """,
        (news, result)
    )

    conn.commit()
    conn.close()


def get_predictions():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM predictions ORDER BY id DESC"
    )

    data = cursor.fetchall()

    conn.close()

    return data


if __name__ == "__main__":
    create_table()
    print("Database created successfully!")