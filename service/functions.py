def chunks(array: list, chunk: int):
    for i in range(0, len(array), chunk):
        yield array[i:i + chunk]


def convert_to_bin(num: int, zerofill: int) -> str:
    return bin(num)[2:].zfill(zerofill)[::-1]

