import sqlite3

conn = sqlite3.connect('db/coinParser.db', check_same_thread=False)
cursor = conn.cursor()


def db_table_val(user_id: int, user_name: str, user_pref: str):
    cursor.execute('INSERT INTO usersTable (user_id, user_name, user_pref) VALUES (?, ?, ?)',
                   (user_id, user_name, user_pref))
    conn.commit()
