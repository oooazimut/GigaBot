import sqlite3 as sq
from datetime import date, timedelta

def remove_old_data():
    tables = [
        "gas_levels",
        "connection",
        "pressures",
        "tank_levels",
        "pumpwork",
        "bypasses",
    ]

    interval = date.today() - timedelta(days=90)

    with sq.connect("Giga.db") as conn:
        for t in tables:
            conn.execute(
                f"delete from {t} where DATE(dttm) < ?",
                [interval],
            )
            print(t, "почищена")
        conn.commit()
        print("ok")


if __name__ == "__main__":
    remove_old_data()
