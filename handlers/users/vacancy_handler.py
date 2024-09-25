from aiogram import F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from loader import dp
from states.states_level import VacancyState
from config.config import TOKEN, HR

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

@dp.callback_query(F.data.startswith('vacancy'))
async def vacancy_callback_query_handler(call: CallbackQuery, state: FSMContext):
    data = call.data.split(":")[-1]
    await state.update_data(vacancy=data)
    await call.message.answer("FIO kiriting")
    await state.set_state(VacancyState.fio)

@dp.message(VacancyState.fio)
async def fio_handler(message: Message, state: FSMContext):
    fio = message.text
    await state.update_data(fio=fio)
    await message.answer("Resume kiriting")
    await state.set_state(VacancyState.resume)

@dp.message(VacancyState.resume)
async def resume_handler(message: Message, state: FSMContext):
    resume = message.text
    await state.update_data(resume=resume)
    await message.answer("Telefon raqamingizni kiriting")
    await state.set_state(VacancyState.number)

@dp.message(VacancyState.number)
async def number_handler(message: Message, state: FSMContext):
    number = message.text
    await state.update_data(number=number)

    data = await state.get_data()
    vacancy = data.get('vacancy')
    fio = data.get('fio')
    resume = data.get('resume')
    number = data.get('number')

    matn = f"FIO: {fio}\nResume: {resume}\nNomer: {number}"
    await message.answer(matn)
    await bot.send_message(chat_id=HR, text=matn)

    await message.answer('Resume adminga yuborildi :)')
    await message.delete()
    await state.clear()