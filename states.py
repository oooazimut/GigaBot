from aiogram.filters.state import StatesGroup, State

class MenuSG(StatesGroup):
    main = State()

class G_sensSG(StatesGroup):
    main = State(),
    prob_sens = State(),
    archive = State()
class Press_sensSG(StatesGroup):
    main = State(),
class UzaSG(StatesGroup):
    main = State(),

class Avail_SG(StatesGroup):
    main = State(),

class Engine_operatingSG(StatesGroup):
    main = State(),