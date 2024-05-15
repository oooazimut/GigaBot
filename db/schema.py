DB_name = 'giga_base.db'

CREATE_SCRIPT = '''
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXIST gas_level (
    id INTEGER PRIMARY KEY,
    sensor INTEGER,
    values real,
    date timestamp,
);
CREATE TABLE IF NOT EXIST  connection(
    id INTEGER PRIMARY KEY,
    cnd integer,
    date timestamp
);

COMMIT;    
'''