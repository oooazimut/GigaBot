import asyncio
from PIL import Image
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

import vars
from config import PUMPS_IDS
from db.repo import PumpWorkService, PressureService
from service.functions import convert_to_bin
from service.plot import PlotService, ImageService
from states import PumpWorkSG, UzaSG


async def on_pumpwork(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = await PumpWorkService.get_current()
    data = [round(int(val) / 60, 1) for val in data]
    plot_path = PlotService.plot_current_pump(data, "Наработка (часы)")
    await manager.start(state=PumpWorkSG.main, data={"path": plot_path})


async def on_uza(cq: CallbackQuery, button: Button, manager: DialogManager):
    imaga = Image.new("RGBA", (1000, 1400), (255, 255, 255))

    pressures, pumpworks = await asyncio.gather(
        PressureService.get_last_values(),
        PumpWorkService.get_current(),
    )

    uzas = convert_to_bin(vars.uzas, zerofill=6)
    uzas = enumerate(uzas, start=1)
    # await ImageService.paste_row(imaga, uzas, "tongs", 100, step=150)

    shifters = enumerate(vars.shifters, start=1)
    # await ImageService.paste_row(imaga, shifters, "shifters", 350, step=150)

    permissions = convert_to_bin(vars.permissions, zerofill=4)
    permissions.append(permissions[-1])
    permissions = list(zip(PUMPS_IDS, permissions))
    permissions.reverse()
    # await ImageService.paste_row(
    #     imaga, permissions, "condition", 600, abcissa=50, size=100
    # )

    await asyncio.gather(
        ImageService.paste_row(imaga, uzas, "tongs", 100, step=150),
        ImageService.paste_row(imaga, shifters, "shifters", 350, step=150),
        ImageService.paste_row(imaga, permissions, "condition", 600, abcissa=50, size=100),
            )

    pumps = convert_to_bin(vars.pumps, zerofill=5)
    pumps = list(zip(PUMPS_IDS, pumps))
    pumps.reverse()
    img_path = await ImageService.paste_row(imaga, pumps, "pumps", 850)

    if pressures:
        pressures = [round(i["value"], 1) for i in pressures]
        pressures = [str(i) for i in pressures]
        pressures.reverse()
    else:
        pressures = ['']* len(PUMPS_IDS)
    pumpworks = await PumpWorkService.get_current()
    pumpworks = [str(round(int(i) / 60, 1)) for i in pumpworks]

    # await ImageService.print_text(imaga, ["Давление(бар)"], (50, 1000), fontsize=40)
    # await ImageService.print_text(imaga, pressures, (50, 1100))
    # await ImageService.print_text(imaga, ["Наработка(часы)"], (50, 1200), fontsize=40)
    # await ImageService.print_text(imaga, pumpworks, (50, 1300))

    await asyncio.gather(
        ImageService.print_text(imaga, ["Давление(бар)"], (50, 1000), fontsize=40),
        ImageService.print_text(imaga, pressures, (50, 1100)),
        ImageService.print_text(imaga, ["Наработка(часы)"], (50, 1200), fontsize=40),
        ImageService.print_text(imaga, pumpworks, (50, 1300))
            )

    await manager.start(UzaSG.main, data={"path": img_path})
