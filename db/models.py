from collections.abc import Callable
import sqlite3 as sq
from typing import Any

from config import DB_NAME


# для нечуствительности кириллицы к регистру


class SqLiteDataBase:
    # def __init__(self, name, script):
    #     self.name = name
    #     with sq.connect(self.name) as con:
    #         con.executescript(script)

    @staticmethod
    def custom_lower(some_str: str):
        return some_str.lower()

    # коннектор к БД
    @staticmethod
    def connector(func: Callable):
        def wrapper(cls, *args, **kwargs) -> list[Any]:
            with sq.connect(
                DB_NAME, detect_types=sq.PARSE_COLNAMES | sq.PARSE_DECLTYPES
            ) as con:
                result = func(cls, con, *args, **kwargs)
                return result

        return wrapper

    # создание БД
    @classmethod
    @connector
    def create(cls, con: sq.Connection, script):
        con.executescript(script)

    # получить из БД
    @classmethod
    @connector
    def select_query(cls, con: sq.Connection, query: str, params=None) -> list[Any]:
        if params is None:
            params = []
        con.create_function("my_lower", 1, cls.custom_lower)
        con.row_factory = sq.Row
        temp = con.execute(query, params).fetchall()
        result = []
        if temp:
            for i in temp:
                item = dict(zip(i.keys(), tuple(i)))
                result.append(item)
        return result

    # положить в БД
    @classmethod
    @connector
    def post_query(cls, con: sq.Connection, query: str, params=None) -> Any | None:
        if params is None:
            params = []
        con.row_factory = sq.Row
        data = con.execute(query, params).fetchall()
        if data:
            data = data[0]
        con.commit()
        return data

    @classmethod
    @connector
    def post_many(cls, con: sq.Connection, query: str, data: list[tuple]):
        for item in data:
            con.executemany(query.format(item[0]), item[1])
