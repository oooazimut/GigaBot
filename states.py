from aiogram.filters.state import StatesGroup, State


class MenuSG(StatesGroup):
    main = State()

class Press_sensSG(StatesGroup):
    main = State(),

class GasSensorsSG(StatesGroup):
    main = State()
    prob_sens = State()
    pump_sens = State()
    archive = State()
    current = State()
    p_val_sens = State()


class PressuresSG(StatesGroup):
    main = State()
    current = State()
    pump_choise = State()
    archive = State()

class UzaSG(StatesGroup):
    main = State()


class AvailSG(StatesGroup):
    main = State()


class PumpWorkSG(StatesGroup):
    main = State()
