import emoji
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import buy_callback, like_callback, dislike_callback


def get_item_keyboard(item_id):
    item_keyboard = InlineKeyboardMarkup()

    buy_button = InlineKeyboardButton(text='Купить товар',
                                      callback_data=buy_callback.new(item_id=item_id))
    item_keyboard.add(buy_button)

    like_button = InlineKeyboardButton(text=emoji.emojize(':thumbsup:', use_aliases=True),
                                       callback_data=like_callback.new(item_id=item_id))
    dislike_button = InlineKeyboardButton(text=emoji.emojize(':thumbsdown:', use_aliases=True),
                                          callback_data=dislike_callback.new(item_id=item_id))
    item_keyboard.add(like_button, dislike_button)

    forward_button = InlineKeyboardButton(text='Поделиться с другом', switch_inline_query=item_id)
    item_keyboard.add(forward_button)
    return item_keyboard
