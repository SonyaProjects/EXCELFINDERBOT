from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import types
from ex import search_pass_name, search_pass_id
from loader import dp


class Mydialog(StatesGroup):
    wait_name = State()
    wait_id = State()


@dp.message_handler(text='поиск')
@dp.message_handler(commands='search_by_name')
async def cmd_dialog_name(message: types.Message):
    await Mydialog.wait_name.set()
    await message.reply("Введите ФИО пользователя")


@dp.message_handler(state=Mydialog.wait_name)
async def get_name(message: Message, state: FSMContext):
    otvet = search_pass_name(message.text)
    await message.answer(text=otvet)
    await state.reset_state()


@dp.message_handler(commands='search_by_id')
async def cmd_dialog_id(message: types.Message):
    await Mydialog.wait_id.set()
    await message.reply("Введите ИНН пользователя")


@dp.message_handler(state=Mydialog.wait_id)
async def get_name(message: Message, state: FSMContext):
    otvet = search_pass_id(message.text)
    await message.answer(text=otvet)
    await state.reset_state()
