import logging

from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from keyboards.inline.callback_data import buy_callback, like_callback, dislike_callback
from keyboards.inline.item_buttons import get_item_keyboard
from loader import dp

items = [
    {'id': '0', 'name': 'Мультиметр Fluke 106', 'rating': 0,
     'link': f'http://cdn.flukeshop.ru/image/cache/370-370/fluke-106-palm-sized-digital-multimeter-300dpi'
             f'-67x100mm-d-nr-15730.jpg'},
    {'id': '1', 'name': 'Клещи Fluke 302+', 'rating': 0,
     'link': f'http://cdn.flukeshop.ru/image/cache/370-370/data/Fluke302+.jpg'}
]


@dp.message_handler(Command('items'))
async def get_items(message: Message):
    for item in items:
        await message.answer_photo(item['link'], caption=item['name'],
                                   reply_markup=get_item_keyboard(item['id']))


@dp.callback_query_handler(buy_callback.filter())
async def buy_item(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=1)
    logging.info(f'{callback_data=}')
    item_id = callback_data.get('item_id')
    await call.message.edit_caption(f'Покупай товар номер {item_id}')


@dp.callback_query_handler(like_callback.filter())
async def like_item(call: CallbackQuery, callback_data: dict):
    logging.info(f'{callback_data=}')
    item_id = callback_data.get('item_id')
    items[int(item_id)]['rating'] += 1
    await call.answer(text=f'Тебе понравился этот товар',
                      show_alert=False, cache_time=0)


@dp.callback_query_handler(dislike_callback.filter())
async def like_item(call: CallbackQuery, callback_data: dict):
    logging.info(f'{callback_data=}')
    item_id = callback_data.get('item_id')
    items[int(item_id)]['rating'] -= 1
    await call.answer(text=f'Тебе не понравился этот товар',
                      show_alert=False, cache_time=0)
