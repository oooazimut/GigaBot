from db.repo import GasSensorService


a = GasSensorService.get_last_values()

print(a)
