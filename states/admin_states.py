from aiogram.fsm.state import State, StatesGroup

class AdminStates(StatesGroup):
    add_category = State()
    add_vacancy = State()

class AddProduct(StatesGroup):
    category = State()
    name = State()
    description = State()
    price = State()
    image = State()