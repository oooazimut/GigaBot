from db.repo import PressureService


data = PressureService.get_last_values()

[print(i) for i in data]