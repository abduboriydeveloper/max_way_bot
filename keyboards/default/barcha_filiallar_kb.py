from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def branches():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='⬅️ Orqaga'), KeyboardButton(text='▶️ Oldinga')],
            [KeyboardButton(text='MAX WAY ALAYSKIY'), KeyboardButton(text='MAX WAY BERUNIY')],
            [KeyboardButton(text='MAX WAY AVIASOZLAR'), KeyboardButton(text='MAX WAY RISOVIY')],
            [KeyboardButton(text='MAX WAY PARUS'), KeyboardButton(text='MAX WAY PARKENT')],
            [KeyboardButton(text='MAX WAY UNIVERSAM'), KeyboardButton(text='MAX WAY ROYSON')],
            [KeyboardButton(text='MAX WAY MUQUMIY'), KeyboardButton(text='MAX WAY GRAND MIR')]
        ],
        resize_keyboard=True
    )
def branches2():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='⬅️ Orqaga'), KeyboardButton(text='MAX WAY SAYRAM')],
            [KeyboardButton(text='MAX WAY MAKSIM GORKIY'), KeyboardButton(text='MAX WAY SERGELI')],
            [KeyboardButton(text='MAX WAY FONTAN'), KeyboardButton(text='MAX WAY MINOR')]
        ],
        resize_keyboard=True
    )

def all_branches():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='⬅️Orqaga'), KeyboardButton(text='▶️Oldinga')],
            [KeyboardButton(text='MAX WAY ALAYSKIY'), KeyboardButton(text='MAX WAY BERUNIY')],
            [KeyboardButton(text='MAX WAY AVIASOZLAR'), KeyboardButton(text='MAX WAY RISOVIY')],
            [KeyboardButton(text='MAX WAY PARUS'), KeyboardButton(text='MAX WAY PARKENT')],
            [KeyboardButton(text='MAX WAY UNIVERSAM'), KeyboardButton(text='MAX WAY ROYSON')],
            [KeyboardButton(text='MAX WAY MUQUMIY'), KeyboardButton(text='MAX WAY GRAND MIR')]
        ],
        resize_keyboard=True
    )
def all_branches2():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='⬅️ Orqaga'), KeyboardButton(text='MAX WAY SAYRAM')],
            [KeyboardButton(text='MAX WAY MAKSIM GORKIY'), KeyboardButton(text='MAX WAY SERGELI')],
            [KeyboardButton(text='MAX WAY FONTAN'), KeyboardButton(text='MAX WAY MINOR')]
        ],
        resize_keyboard=True
    )