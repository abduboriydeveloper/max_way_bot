from aiogram import F
from aiogram.types import Message

from loader import dp


@dp.message(F.text == 'MAX WAY ALAYSKIY')
async def get_branch1(message: Message):
    text = '📍 Filial:  MAX WAY ALAYSKIY \n\n🗺 Manzil:  проспект Амира Темура, 25\n\n🏢 Orientir:\n\n☎️ Telefon raqami:  +998712005400\n\n🕙 Ish vaqti : 10:00 - 03:00'
    
    await message.answer(text)
    await message.answer_location(
        latitude=41.318379,
        longitude=69.280708
    )


@dp.message(F.text == 'MAX WAY BERUNIY')
async def beruniy_branch(message: Message):
    await message.answer('''📍 Filial:  MAX WAY BERUNIY 
                     
🗺 Manzil:  улица Беруни, 47, Ташкент 
                     
🏢 Orientir:  Метро Беруний 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 23:00''')
    await message.answer_location(latitude=41.344430, longitude=69.205021)

@dp.message(F.text == 'MAX WAY AVIASOZLAR ')
async def aviasozlar_branch(message: Message):
    await message.answer('''📍 Filial:  MAX WAY AVIASOZLAR 
                     
🗺 Manzil:  улица Авиасозлар, 23 
                     
🏢 Orientir:   
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00''')
    await message.answer_location(latitude=41.290894,longitude=69.342153)

@dp.message(F.text == 'MAX WAY RISOVIY')
async def risoviy_branch(message: Message):
    await message.answer('''📍 Filial:  MAX WAY RISOVIY 
                     
🗺 Manzil:  Узбекистан, Ташкент, Алтынкульская улица, 10 
                     
🏢 Orientir:  банкетный зал Тантана 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00''')
    await message.answer_location(latitude=41.274899,longitude=69.309423)

@dp.message(F.text == 'MAX WAY PARUS')
async def parus_branch(message: Message):
    await message.answer('''📍 Filial:  MAX WAY PARUS 
                     
🗺 Manzil:  улица Катартал, 60/5 
                     
🏢 Orientir:  ТЦ Парус 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00''')
    await message.answer_location(latitude=41.293536,longitude=69.212856)

@dp.message(F.text == 'MAX WAY PARKENT')
async def parkent_branch(message: Message):
    await message.answer('''📍 Filial:  MAX WAY PARKENT 
                     
🗺 Manzil:  улица Паркент, 30В, Ташкент 
                     
🏢 Orientir:  Паркентский рынок 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00''')
    await message.answer_location(latitude=41.363468,longitude=69.288586)

@dp.message(F.text == 'MAX WAY UNIVERSAM')
async def universam_branch(message: Message):
    await message.answer('''📍 Filial:  MAX WAY UNIVERSAM 
                     
🗺 Manzil:  Узбекистан, Ташкент, проспект Амира Темура, 41/3 
                     
🏢 Orientir:  Ориентир: Юнусабад Универсам 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 23:00''')
    await message.answer_location(latitude=41.363468,longitude=69.288586)

@dp.message(F.text == 'MAX WAY ROYSON')
async def royson_branch(message: Message):
    await message.answer('''📍 Filial:  MAX WAY ROYSON 
                     
🗺 Manzil:  Узбекистан, Ташкент, улица Заркайнар, 2 
                     
🏢 Orientir:  Ориентир: Цирк 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 01:00''')
    await message.answer_location(latitude=41.322643,longitude=69.241973)

@dp.message(F.text == 'MAX WAY MUQUMIY')
async def muqumiy_branch(message: Message):
    await message.answer('''📍 Filial:  MAX WAY MUQUMIY 
                     
🗺 Manzil:  улица Чиланзар, Ташкент 
                     
🏢 Orientir:  Ориентир: Чиланзар 1-й квартал 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 04:00''')
    await message.answer_location(latitude=41.287875,longitude=69.229238)

@dp.message(F.text == 'MAX WAY GRAND MIR')
async def grand_mir_branch(message: Message):
    await message.answer('''📍 Filial:  MAX WAY GRAND MIR 
                     
🗺 Manzil:  Узбекистан, Ташкент, улица Шота Руставели, 9А 
                     
🏢 Orientir:  Ориентир: Гостиница Гранд Мир 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 04:00''')
    await message.answer_location(latitude=41.295095,longitude=69.267970)

@dp.message(F.text == 'MAX WAY SAYRAM')
async def sayram_branch(message:Message):
    await message.answer('''📍 Filial:  MAX WAY SAYRAM 
                     
🗺 Manzil:  Узбекистан, Ташкент, улица Юнусота 
                     
🏢 Orientir:  Ориентир: Рынок сайрам.  
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00''')
    await message.answer_location(latitude=41.371941,longitude=69.310594)

@dp.message(F.text == 'MAX WAY MAKSIM GORKIY')
async def maksim_branch(message:Message):
    await message.answer('''📍 Filial:  MAX WAY MAKSIM GORKIY 
                     
🗺 Manzil:  махалля Элобод 
                     
🏢 Orientir:  Ориентир: Метро буюк ипак йули 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 01:00''')
    await message.answer_location(latitude=41.327072,longitude=69.329893)

@dp.message(F.text == 'MAX WAY SERGELI')
async def sergeli_branch(message:Message):
    await message.answer('''📍 Filial:  MAX WAY SERGELI 
                     
🗺 Manzil:  Узбекистан, Ташкент, Сергелийский район, массив Сергели-VIIIА, 11 
                     
🏢 Orientir:  Ориентир: Сергели Дехкон Бозори 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00''')
    await message.answer_location(latitude=41.226369,longitude=69.219899)

@dp.message(F.text == 'MAX WAY FONTAN')
async def fontan_branch(message:Message):
    await message.answer('''📍 Filial:  MAX WAY FONTAN 
                     
🗺 Manzil:  проспект Амира Темура 
                     
🏢 Orientir:  Ориентир: Юнусабадский рынок 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00''')
    await message.answer_location(latitude=41.362917,longitude=69.288864)

@dp.message(F.text == 'MAX WAY MINOR')
async def minor_branch(message:Message):
    await message.answer('''📍 Filial:  MAX WAY MINOR 
                     
🗺 Manzil:  улица Осиё, 84А, Юнусабадский район, Ташкент 
                     
🏢 Orientir:  бывший кинотеатр Казахстан 
                     
☎️ Telefon raqami:  +998712005400
                     
🕙 Ish vaqti : 10:00 - 03:00''')
    await message.answer_location(latitude=41.328054,longitude=69.282584)
