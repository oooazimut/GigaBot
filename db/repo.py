from db.models import SqLiteDataBase
from db.schema import DB_NAME, CREATE_SCRIPT
from config import PUMPS_IDS

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

        # current_date = datetime.datetime.now()
        # delta: datetime.timedelta = current_date - result[0]['dttm']
        # if delta.seconds > 300:
        #     return

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


class PumpWorkService(Service):
    @staticmethod
    def get_current():
        with open('vars.txt', 'r') as file:
            data = file.read().split()
        result = dict(zip(PUMPS_IDS, data))
        return result
