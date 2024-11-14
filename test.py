import sqlite3


script = "update gas_levels set name = ? where name = ?"
data = [
    ("5.1", "насосная.1"),
    ("5.2", "насосная.2"),
    ("5.4", "насосная.3"),
    ("5.3", "насосная.4"),
    ("3.8", "пробная.1"),
    ("4.1", "пробная.2"),
]

with sqlite3.connect("Giga.db") as con:
    con.executemany(script, data)
