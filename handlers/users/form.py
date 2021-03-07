from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states import Form


@dp.message_handler(Command("form"), state=None)
async def form_start(message: types.Message):
    await message.answer(f'Пожалуйста, введите имя.')

    await Form.before_name.set()


@dp.message_handler(state=Form.before_name)
async def enter_name(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer(f'Теперь, пожалуйста, e-mail.')

    await Form.before_email.set()


@dp.message_handler(state=Form.before_email)
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer(f'Теперь, пожалуйста, номер телефона.')

    await Form.before_phone.set()


@dp.message_handler(state=Form.before_phone)
async def enter_phone(message: types.Message, state: FSMContext):
    phone = message.text
    await state.update_data(phone=phone)
    form = await state.get_data()
    await message.answer(f"""
Привет! Ты ввел следующие данные:

Имя - {form['name']}

Email - {form['email']}

Телефон: - {form['phone']}
""")

    await state.reset_state()
