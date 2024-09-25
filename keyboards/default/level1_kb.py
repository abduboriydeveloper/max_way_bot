from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def language_buttons():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='O’zbekcha'), 
                KeyboardButton(text='Русский'), 
                KeyboardButton(text='English')]
        ]
    )

def menu_buttons():
    return ReplyKeyboardMarkup(
        keyboard= [
        [KeyboardButton(text="🛍Buyurtma Berish")],
        [KeyboardButton(text="🎉Aksiya"),KeyboardButton(text="🏘Barcha filiallar")],
        [KeyboardButton(text="📋Mening Buyurtmalarim"),KeyboardButton(text="✍️Izoh qoldirish")],
        [KeyboardButton(text="💼Vakansiyalar"),KeyboardButton(text="ℹ️Biz haqimizda")]
        ],
        resize_keyboard=True
    )