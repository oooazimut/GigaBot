from config import PUMPS_IDS
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

        # current_date = datetime.datetime.now()
        # delta: datetime.timedelta = current_date - result[0]['dttm']
        # if delta.seconds > 300:
        #     print(delta.seconds)
        #     return

        return result


class PumpWorkService(Service):
    @staticmethod
    def get_current():
        with open('vars.txt', 'r') as file:
            data = file.read().split()
        result = dict(zip(PUMPS_IDS, data))
        return result
