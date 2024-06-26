import datetime

from db.models import SqLiteDataBase
from db.schema import DB_NAME, CREATE_SCRIPT

db = SqLiteDataBase(DB_NAME, CREATE_SCRIPT)


class Service:
    @staticmethod
    def save_to_table(table: str, params: list):
        query = f'INSERT INTO {table} (name, value, dttm) VALUES (?, ?, ?)'
        db.post_query(query, params=params)


class PressureService(Service):
    @staticmethod
    def get_last_values():
        query = 'SELECT * from (SELECT * FROM pressures ORDER BY id DESC LIMIT 5) ORDER BY name'
        result = db.select_query(query)

        current_date = datetime.datetime.now()
        delta: datetime.timedelta = current_date - result[0]['dttm']
        if delta.seconds > 300:
            return

        el3 = result.pop()
        result.insert(2, el3)
        return result

    @staticmethod
    def get_values_by_date(date, pump=None):
        query = 'select * from pressures where date(dttm) = ?'
        params = [date]
        if pump:
            query += ' AND name = ?'
            params.append(pump)
        result = db.select_query(query, params)
        return result


class GasSensorService(Service):
    @staticmethod
    def get_last_values():
        query = ('SELECT * from (SELECT * FROM gas_levels  WHERE name like "пробная%" ORDER BY dttm DESC LIMIT 5) '
                 'GROUP BY name')
        result = db.select_query(query)

        current_date = datetime.datetime.now()
        delta: datetime.timedelta = current_date - result[0]['dttm']
        if delta.seconds > 300:
            return

        return result

    @staticmethod
    def get_archive_values(date, g_sens=None):
        query = 'select * from gas_levels where date(dttm) = ?'
        params = [date]
        if g_sens:
            query += ' AND name like ?'
            params.append(g_sens)
        result = db.select_query(query, params)
        return result

    @staticmethod
    def get_g_pumps_last_values():
        query = ('SELECT * from (SELECT * FROM gas_levels  WHERE name like "насосная%" ORDER BY dttm DESC LIMIT 5) '
                 'GROUP BY name')
        result = db.select_query(query)

        # current_date = datetime.datetime.now()
        # delta: datetime.timedelta = current_date - result[0]['dttm']
        # if delta.seconds > 300:
        #     print(delta.seconds)
        #     return

        return result

    @staticmethod
    def get_g_sens_warning_values():
        query = 'SELECT * from gas_levels'
        result = db.select_query(query)
        return result


class PumpWorkService(Service):
    @staticmethod
    def get_current() -> list:
        with open('pumpwork.txt', 'r') as file:
            data = file.read().split()
        data.reverse()
        return data


class UserService(Service):
    @staticmethod
    def get_user(userid):
        query = 'SELECT * FROM users WHERE id = ?'
        result = db.select_query(query, [userid])
        return result

    @staticmethod
    def insert_user(userid, username):
        query = 'INSERT INTO users (id, name) VALUES (?, ?)'
        db.post_query(query, [userid, username])
