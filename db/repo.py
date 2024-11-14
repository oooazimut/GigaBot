import datetime

from db.models import SqLiteDataBase as SqDB


class Service:
    @staticmethod
    def save_to_table(table: str, params: list):
        query = f"INSERT INTO {table} (name, value, dttm) VALUES (?, ?, ?)"
        SqDB.post_query(query, params=params)

    @staticmethod
    def save_to_tables(data: list):
        query = "INSERT INTO {} (name, value, dttm) VALUES (?, ?, ?)"
        SqDB.post_many(query, data)


class PressureService(Service):
    @staticmethod
    async def get_last_values():
        query = """
          SELECT * 
            FROM (
                SELECT * 
                  FROM pressures 
              ORDER BY id DESC LIMIT 5
              ) 
        ORDER BY name
        """
        result = SqDB.select_query(query)

        current_date = datetime.datetime.now()
        delta: datetime.timedelta = current_date - result[0]["dttm"]
        if delta.seconds > 300:
            return

        el3 = result.pop()
        result.insert(2, el3)
        return result

    @staticmethod
    def get_values_by_date(date, pump=None):
        query = "select * from pressures where date(dttm) = ?"
        params = [date]
        if pump:
            query += " AND name = ?"
            params.append(pump)
        result = SqDB.select_query(query, params)
        return result


class GasSensorService(Service):
    @staticmethod
    def get_last_values():
        query = "SELECT name, round(value, 1) as value, dttm from gas_levels WHERE dttm = (SELECT max(dttm) from gas_levels)"
        result = SqDB.select_query(query)
        current_date = datetime.datetime.now()
        delta: datetime.timedelta = current_date - result[0]["dttm"]

        if delta.seconds > 300:
            return

        return {i["name"]: i["value"] for i in result}

    @staticmethod
    def get_archive_values(date, g_sens=None):
        query = "select * from gas_levels where date(dttm) = ?"
        params = [date]
        if g_sens:
            placeholders = ', '.join(['?']*len(g_sens))
            query += f" AND name in ({placeholders})"
            params.extend(g_sens)
        result = SqDB.select_query(query, params)
        return result

    @staticmethod
    def get_g_sens_warning_values():
        query = "SELECT * from gas_levels"
        result = SqDB.select_query(query)
        return result


class PumpWorkService(Service):
    @staticmethod
    async def get_current() -> list:
        with open("pumpwork.txt", "r") as file:
            data = file.read().split()
        data.reverse()
        return data


class UserService(Service):
    @staticmethod
    def get_user(userid):
        query = "SELECT * FROM users WHERE id = ?"
        result = SqDB.select_query(query, [userid])
        return result

    @staticmethod
    def insert_user(userid, username):
        query = "INSERT INTO users (id, name) VALUES (?, ?)"
        SqDB.post_query(query, [userid, username])

    @staticmethod
    def get_all_users():
        query = "SELECT * FROM users"
        return SqDB.select_query(query)
