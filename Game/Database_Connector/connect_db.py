import mariadb
import sys

def connect():
    try:
        conn = mariadb.connect(
            user="root",
            password="",
            host="127.0.0.1",
            port=3342,
            database="pokemon_battle"

        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    print("Connected to MariaDB Platform!")

    cur = conn.cursor()

    return cur