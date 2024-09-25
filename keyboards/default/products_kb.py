from loader import db
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def make_product_kb(category_name:str):
    products = db.get_products_by_category_name(category_name)
    buttons = []
    menu = ReplyKeyboardMarkup(keyboard=[], resize_keyboard=True ,row_width = 15)

    for product in products:
        buttons.append(
            KeyboardButton(text=product[0])
        )
    menu.keyboard.append(
        buttons
    )

    return menu

def make_cart_kb():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="◀️ Orqaga")],
        [KeyboardButton(text="📥 Savat")]
        ],
        resize_keyboard=True
    )