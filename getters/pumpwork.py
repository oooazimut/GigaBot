from db.repo import PumpWorkService


async def current_getter(**kwargs):
    data = PumpWorkService.get_current()
    return data