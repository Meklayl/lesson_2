from aiogram import types,executor,Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import reg_menu


class Registration(StatesGroup):
    name = State()
    last_name = State()
    phone_num =State()
    email = State()
    adress = State()
    birth_date = State()


PROXY_URL = "http://proxy.server:3128/"
bot = Bot("7212688567:AAEl4mOIfET0mVAGXUZc9WdvosbnN7iXm1",proxy=PROXY_URL)
storage  = MemoryStorage()
dp = Dispatcher(bot,storage=storage)


@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    await message.answer('''Assalamu aleykum, botimizga xosh keldiniz
Registraciydan otiw ushin tomendegi tuymeni
basin''',reply_markup=reg_menu)


@dp.callback_query_handler()
async def send_reg(call:types.CallbackQuery):
    data = call.data
    if data == 'reg':
        await bot.send_message(
            chat_id=call.from_user.id,
            text='OOO, taza qolllaniwshi. \nBizge atinzidi jazip jiberin'
        )
        await Registration.name.set()


@dp.message_handler(state=Registration.name)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['name']=message.text
    await message.answer('Axa, endi bizde familiyanizdi jazip jazip qaldirin:')
    await Registration.last_name.set()


@dp.message_handler(state=Registration.last_name)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['last_name']=message.text
    await message.answer('Axa, endi bizde telefon nomerinizdi jazip jazip qaldirin:')
    await Registration.phone_num.set()


@dp.message_handler(state=Registration.phone_num)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['phone_num']=message.text
    await message.answer('Axa, endi bizde email adresinizdi  jazip jazip qaldirin:')
    await Registration.email.set()


@dp.message_handler(state=Registration.email)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['email']=message.text
    await message.answer('Axa, endi bizde tuwilgan jilinizdi jazip jazip qaldirin:')
    await Registration.birth_date.set()


@dp.message_handler(state=Registration.birth_date)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['birth_date']=message.text
    await message.answer('Axa, endi bizde adresinizdi jazip jazip qaldirin:')
    await Registration.adress.set()


@dp.message_handler(state=Registration.adress)
async def send_name(message:types.Message,state:FSMContext):
    async with state.proxy() as magliwmat:
        magliwmat['adress']=message.text
    await message.answer(f'''Siz registraciyani jumaqladiniz.
Ati:{magliwmat['name']},
Familiyasi:{magliwmat['last_name']},
Telefon nomeri:{magliwmat['phone_num']},
Jili:{magliwmat['birth_date']},
adresi:{magliwmat['adress']},
email:{magliwmat['email']}
''')
    state.finish()


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)