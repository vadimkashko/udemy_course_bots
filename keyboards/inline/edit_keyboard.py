from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline.callback_data import edit_callback

edit = InlineKeyboardMarkup(row_width=2)

edit_name = InlineKeyboardButton(text='Edit Name', callback_data=edit_callback.new(object='name'))
edit.insert(edit_name)

edit_description = InlineKeyboardButton(text='Edit Description',
                                        callback_data=edit_callback.new(object='description'))
edit.insert(edit_description)

edit_about = InlineKeyboardButton(text='Edit About', callback_data=edit_callback.new(object='about'))
edit.insert(edit_about)

edit_botpic = InlineKeyboardButton(text='Edit Botpic', callback_data=edit_callback.new(object='botpic'))
edit.insert(edit_botpic)

edit_commands = InlineKeyboardButton(text='Edit Commands',
                                     callback_data=edit_callback.new(object='commands'))
edit.insert(edit_commands)

back_to_bot = InlineKeyboardButton(text='<<Back to Bot', callback_data=edit_callback.new(object='back'))
edit.insert(back_to_bot)
