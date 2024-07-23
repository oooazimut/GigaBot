import sqlite3 as sq

with sq.connect('Giga.db') as con:
    con.execute('delete from tank_levels where name > 3')
