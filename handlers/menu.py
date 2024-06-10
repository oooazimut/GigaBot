from PIL import Image
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

import vars
from config import PUMPS_IDS
from db.repo import PumpWorkService
from service.functions import convert_to_bin
from service.plot import PlotService, ImageService
from states import PumpWorkSG, UzaSG


async def on_pumpwork(cq: CallbackQuery, button: Button, manager: DialogManager):
    data = PumpWorkService.get_current()
    data = [round(int(val) / 3600, 1) for val in data]
    plot_path = PlotService.plot_current_pump(data, 'Наработка (часы)')
    await manager.start(state=PumpWorkSG.main, data={'path': plot_path})


async def on_uza(cq: CallbackQuery, button: Button, manager: DialogManager):
    imaga = Image.new('RGBA', (1000, 1000), (255, 255, 255))

    uzas = map(int, convert_to_bin(vars.uzas, zerofill=6))
    uzas = enumerate(uzas, start=1)
    ImageService.paste_row(imaga, uzas, 'tongs', 100, step=150)

    shifters = enumerate(vars.shifters, start=1)
    ImageService.paste_row(imaga, shifters, 'shifters',  350, step=150)

    permissions = list(map(int, convert_to_bin(vars.permissions, zerofill=4)))
    permissions.append(permissions[-1])
    permissions = list(zip(PUMPS_IDS, permissions))
    permissions.reverse()
    ImageService.paste_row(imaga, permissions, 'condition', 600, abcissa=50, size=100)

    pumps = map(int, convert_to_bin(vars.pumps, zerofill=5))
    pumps = list(zip(PUMPS_IDS, pumps))
    pumps.reverse()
    img_path = ImageService.paste_row(imaga, pumps, 'pumps', 850)

    await manager.start(UzaSG.main, data={'path': img_path})
