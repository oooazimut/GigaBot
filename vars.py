from config import GAS_SENS_DESCS, GAS_SENS_PROB_DESCS, PUMPS_IDS

uzas = 0
permissions = 0
pumps = 0
shifters = []
sirens = dict()
levels = {1: 0, 2: 0, 3: 0}
cheats = {key: 0 for key in PUMPS_IDS}
gas_sensors = {key: False for key in GAS_SENS_DESCS + GAS_SENS_PROB_DESCS}
