from aiogram import F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


from loader import dp, db
from keyboards.default.level2_kb import for_buyurtma_berish_kb, for_yetkazib_berish_kb
from keyboards.default.barcha_filiallar_kb import branches, branches2, all_branches, all_branches2
from keyboards.default.products_kb import make_product_kb, make_cart_kb
from states.states_level import BuyurtmaBerishState
from keyboards.default.categories_kb import get_categories_kb
from keyboards.inline.vacancy_kb import make_vacancy_kb
from keyboards.inline.product_inline_kb import make_product_plus_minus, make_cart_extra_kb
from keyboards.inline.categories_kb import make_category_kb_for_admin

@dp.message(F.text == '🛍Buyurtma Berish')
async def buyurtma_berish(message: Message, state: FSMContext):
    await message.answer('Yetkazib berish turini tanlang', reply_markup=for_buyurtma_berish_kb())

@dp.message(F.text == '🎉Aksiya')
async def aksiya(message: Message , state: FSMContext):
    await message.answer('Hozirgi vaqtda hech qanday aksiyalar yoq')

@dp.message(F.text == '🏘Barcha filiallar')
async def all_fillials(message: Message , state: FSMContext):
    await message.answer('Bizning filiallarimiz :',reply_markup=branches())

@dp.message(F.text == '📋Mening Buyurtmalarim')
async def my_orders(message: Message , state: FSMContext):
    await message.answer('Sizda buyurtmalar yoq')

@dp.message(F.text == '✍️Izoh qoldirish')
async def izoh_qoldirish(message: Message , state: FSMContext):
    await message.answer('Izoh qoldiring. Sizning fikringiz biz uchun muhim')

@dp.message(F.text == 'ℹ️Biz haqimizda')
async def about_us(message: Message , state: FSMContext):
    file = FSInputFile(path='D:\Desktop\max_way\photo_2023-07-24_11-21-37.jpg')
    await message.answer_photo(file, caption='''🍟 Max Way 
☎️ Aloqa markazi: +998712005400''')

@dp.message(F.text == '💼Vakansiyalar')
async def vakansiyalar(message: Message , state: FSMContext):
    vacancies = db.get_vacancies()
    await message.answer('💼 Vakansiyalar:')
    for title in vacancies:
        await message.answer(text=title[0], reply_markup=make_vacancy_kb(title[0]))

@dp.message(F.text=='🏃 Olib ketish')
async def choose_branch(message:Message , state: FSMContext):
    await message.answer('Filialni tanlang', reply_markup=all_branches())

@dp.message(F.text == '▶️ Oldinga')
async def oldinga(message :Message , state: FSMContext):
    await message.answer('Bizning filiallarimiz :',reply_markup=branches2())

# @dp.message(F.text == '▶️Oldinga')

@dp.message(F.text == '🚖 Yetkazib berish')
async def yetkazib_berish(message: Message, state: FSMContext):
    await message.answer('Buyurtmani davom ettirish uchun iltimos lokatsiyangizni yuboring',
                         reply_markup=for_yetkazib_berish_kb())
    
    await state.set_state(BuyurtmaBerishState.yetkazib_berish)

@dp.message(BuyurtmaBerishState.yetkazib_berish)
async def get_user_location_handler(message: Message, state: FSMContext):
    if message.location:
        await message.answer('Kategoriyani tanlang', reply_markup=get_categories_kb())
        await state.set_state(BuyurtmaBerishState.select_category)
    else:
        await message.answer('Iltimos lokatsiya yuboring')

@dp.message(BuyurtmaBerishState.select_category)
async def get_product_category_handler(message:Message, state: FSMContext):
    category_name = message.text
    await state.update_data(category_name=category_name)

    await message.answer('Mahsulotni tanlang', reply_markup=make_product_kb(category_name))
    await state.set_state(BuyurtmaBerishState.product)

async def calculate_price(price, quantity = 1):
    return quantity * price

@dp.message(F.text == "📥 Savat", BuyurtmaBerishState.product)
async def show_cart(message: Message, state: FSMContext):
    tg_id = message.from_user.id
    carts=db.get_user_cart(tg_id)
    main_text = ''
    for cart in carts:
        name, price, quantity= cart
        main_text+=f"{name} x {quantity} = {price*quantity}\n\n Umumiy: {price*quantity}"
    await message.answer("Savat:")
    await message.answer(main_text, reply_markup=make_cart_extra_kb)

@dp.message(BuyurtmaBerishState.product)
async def get_product_handler(message:Message, state: FSMContext):
    product_name = message.text
    await state.update_data(product_name=product_name)
    data = await state.get_data()
    name,description,price,image = db.get_product_by_name(product_name)
    quantity = data.get("quantity")
    if not quantity:
        quantity = 1
    jami = await calculate_price(price, quantity)
    await state.update_data(quantity=quantity, price=price,description = description,name = name)
    caption = f"{name}\n{description}\n\n{name} {price} x {quantity} = {jami}\nUmumiy: {jami}"
    file = FSInputFile(path=image)
    await state.update_data(quantity=1)
    await message.answer_photo(
    photo=file,
    caption=caption,
    reply_markup=make_product_plus_minus()
    )


@dp.callback_query(F.data == "plus", BuyurtmaBerishState.product)
async def product_plus(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    quantity = data.get("quantity")
    price = data.get("price")
    name = data.get("name")
    description = data.get("description")
    quantity+=1

    await call.answer("Mahsulot savatga qo'shildi")
    await state.update_data(quantity=quantity)
    jami = await calculate_price(price, quantity)
    caption = f"{name}\n{description}\n\n{name} {price} x {quantity} = {jami}\nUmumiy: {jami}"
    await call.message.edit_caption(caption=caption, reply_markup=make_product_plus_minus(quantity))


@dp.callback_query(F.data == "minus", BuyurtmaBerishState.product)
async def product_plus(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    quantity = data.get("quantity")
    price = data.get("price")
    name = data.get("name")
    description = data.get("description")
    quantity = data.get("quantity")
    if quantity!=1:
        quantity-=1
        await state.update_data(quantity=quantity)
    jami = await calculate_price(price, quantity)
    await call.answer("Mahsulot savatdan o'chirildi")
    await state.update_data(quantity=quantity)
    caption = f"{name}\n{description}\n\n{name} {price} x {quantity} = {jami}\nUmumiy: {jami}"
    await call.message.edit_caption(caption=caption, reply_markup=make_product_plus_minus(quantity))

@dp.callback_query(F.data == "add_to_cart", BuyurtmaBerishState.product)
async def add_to_cart(call:CallbackQuery, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    quantity = data.get("quantity")
    tg_id = call.from_user.id
    db.add_to_cart(name, quantity, tg_id)
    await call.message.answer("Mahsulot savatga qo'shildi", reply_markup=make_cart_kb())
    await call.message.delete()

@dp.callback_query(F.data == "confirm_order", BuyurtmaBerishState.product)
async def confirm_cart(state: FSMContext, message: Message):
    tg_id = message.from_user.id
    carts=db.get_user_cart(tg_id)
    main_text = ''
    for cart in carts:
        name, price, quantity= cart
        main_text+=f"{name} x {quantity} = {price*quantity}\n\n Umumiy: {price*quantity}"
    # await message.answer(main_text,f"\n Yetkazib berish turi:{}")


@dp.callback_query(F.data == "continiue_order", BuyurtmaBerishState.product)
async def continiue_cart(call:CallbackQuery, state:FSMContext, message: Message):
    category_name = message.text
    await state.update_data(category_name=category_name)

    await message.answer('Mahsulotni tanlang', reply_markup=make_product_kb(category_name))