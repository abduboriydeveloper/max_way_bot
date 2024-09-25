from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def make_product_plus_minus(number = 1):
    menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="+", callback_data="plus"),
                InlineKeyboardButton(text=f"{number}", callback_data=f"number.{number}"),
                InlineKeyboardButton(text="-", callback_data="minus")
            ],
            [
                InlineKeyboardButton(text="Savatga qo'shish", callback_data="add_to_cart")
            ]
        ]
    )
    return menu

def make_cart_extra_kb():
    return InlineKeyboardBuilder(
        inline_keyboard = [
            [
                InlineKeyboardButton(text="Buyurtmani tasdiqlash", callback_data="confirm_order")
            ]
            [
                InlineKeyboardButton(text="Buyurtmani davom ettirish", callback_data="continiue_order")
            ]
            [
                InlineKeyboardButton(text="Tozalash", callback_data="clear_order")
            ]
        ]
    )