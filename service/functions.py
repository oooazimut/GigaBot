from config import PUMPS_IDS


def chunks(array: list, chunk: int):
    for i in range(0, len(array), chunk):
        yield array[i:i + chunk]


def convert_to_bin(num: int, zerofill: int) -> str:
    return bin(num)[2:].zfill(zerofill)[::-1]


def sort_pressures_by_pumps(data):
    result = dict()
    for item in data:
        result.setdefault(item['name'], []).append((item['dttm'], item['value']))

    return result
def sort_gas_sensors(data):
    result = dict()
    for item in data:
        result.setdefault(item['name'], []).append((item['dttm'], item['value']))

    return result

