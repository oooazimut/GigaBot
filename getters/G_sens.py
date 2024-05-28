from config import GAS_SENS_IDS, GAS_SENS_DESCS

async def on_sens_selected(**kwargs):
    g_sens = list(zip(GAS_SENS_IDS, GAS_SENS_DESCS))
    return {'g_sens': g_sens}