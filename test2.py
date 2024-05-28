import sqlite3


def check_database_integrity(db_path):
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Выполняем команду PRAGMA integrity_check
        cursor.execute("PRAGMA integrity_check;")
        result = cursor.fetchone()

        # Проверяем результат
        if result[0] == 'ok':
            print(f"Database '{db_path}' is OK.")
        else:
            print(f"Integrity check failed for database '{db_path}': {result[0]}")

    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()


# Замените 'mydatabase.db' на путь к вашей базе данных
check_database_integrity('Giga.db')