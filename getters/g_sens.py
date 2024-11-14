from config import GAS_SENS_DESCS, GAS_SENS_PROB_DESCS


async def on_sens_selected(**kwargs):
    return {"p_sens": GAS_SENS_DESCS}


async def on_sens_prob_selected(**kwargs):
    return {"g_sens": GAS_SENS_PROB_DESCS}
