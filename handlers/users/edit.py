# import logging

from aiogram import types
from aiogram.dispatcher.filters import Command

# from keyboards.inline.callback_data import edit_callback
from keyboards.inline.edit_keyboard import edit
from loader import dp


@dp.message_handler(Command('inline_buttons_1'))
async def edit_bot(message: types.Message):
    await message.answer(text='Edit @Sberleadbot info.\n\n'
                              'Name: Бот для Заданий на Курсе Udemy\n'
                              'Description: ?\n'
                              'About: ?\n'
                              'Botpic: ? no botpic\n'
                              'Commands: no commands yet',
                         reply_markup=edit)
