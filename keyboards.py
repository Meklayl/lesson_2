from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


reg_menu = InlineKeyboardMarkup()
reg_menu.add(InlineKeyboardButton(text='Registraciya',callback_data='reg'))