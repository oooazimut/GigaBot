from aiogram.filters.state import StatesGroup, State

class menuSG(StatesGroup):
    main = State()

class g_sensSG(StatesGroup):

    main = State(),
    prob_sens = State(),
    archive = State()
