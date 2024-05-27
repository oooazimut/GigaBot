from db.repo import PumpWorkService

data = PumpWorkService.get_current()
print(data)