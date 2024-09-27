from aiogram.fsm.state import StatesGroup, State

import states


class NameFetcher(StatesGroup):
    name_waiting = State()
