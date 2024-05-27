from config import PUMPS_DESCS, PUMPS_IDS
from db.repo import PressureService


async def pumps_choice_getter(**kwargs):
    pumps = list(zip(PUMPS_IDS, PUMPS_DESCS))
    return {'pumps': pumps}
