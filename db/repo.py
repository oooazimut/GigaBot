from db.models import SqLiteDataBase
from db.schema import DB_NAME, CREATE_SCRIPT

db = SqLiteDataBase(DB_NAME, CREATE_SCRIPT)


class Service:
    @staticmethod
    def save_to_table(table: str, params: list):
        query = f'INSERT INTO {table} (name, value, dttm) VALUES (?, ?, ?)'
        db.post_query(query, params=params)
