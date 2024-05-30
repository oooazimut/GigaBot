from aiogram.filters.state import StatesGroup, State


class MenuSG(StatesGroup):
    main = State()

class GasSensorsSG(StatesGroup):
    main = State()
    prob_sens = State()
    pump_sens = State()
    archive = State()
    current = State()
    p_val_sens = State()
    choice_g_sens = State()
    choice_sens = State()
    all_sens = State()
    plot = State()
    archive_pumps = State()
    choice_sens_pump = State()

class PressuresSG(StatesGroup):
    main = State()
    date_choice = State()
    quantity_choice = State()
    pump_choice = State()
    plot = State()

class UzaSG(StatesGroup):
    main = State()


class PumpWorkSG(StatesGroup):
    main = State()
