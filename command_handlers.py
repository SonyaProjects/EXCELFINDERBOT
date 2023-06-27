from user_keyboards import commands_default_keyboard
from aiogram import types
from loader import dp


from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import types
from ex import search_pass_name
from loader import dp


@dp.message_handler(text=['Привет', 'Начать'])
@dp.message_handler(commands=['start'])
async def answer_start_command(message: types.Message):
    await message.answer(text='Привет!'
                         f'\nРад тебя видеть!',
                         reply_markup=commands_default_keyboard)


@dp.message_handler(text=['Помощь'])
@dp.message_handler(commands='help')
async def answer_help_message(message: types.Message):
    await message.answer(text='Этот бот создан специально для поиска номера телефона'
                         f'\nПоиск осуществляется по команде search_by_id'
                         f'\nДля поиска по ИНН'
                         f'\nИли по ФИО'
                         f'\nИспользуя команду search_by_name')


# class Mydialog(StatesGroup):
#     wait_name = State()
#     wait_id = State()  # Will be represented in storage as 'Mydialog:otvet'

# # Здесь мы начинаем общение с клиентом и включаем состояния


# @dp.message_handler(text='поиск')
# @dp.message_handler(commands='search_by_name')
# async def cmd_dialog(message: types.Message):
#     await Mydialog.wait_name.set()  # вот мы указали начало работы состояний (states)
#     await message.reply("Человечишка, напиши мне свое жалкое мнение")


# @dp.message_handler(state=Mydialog.wait_name)
# async def get_name(message: Message, state: FSMContext):
#     # await state.update_data({'name': message.text})
#     otvet = search_pass_name(message.text)
#     await message.answer(text=otvet)
