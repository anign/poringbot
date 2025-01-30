from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.formatting import sizeof

main_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Регистрация', callback_data='register')],
    [InlineKeyboardButton(text='Замки', callback_data='castles')],
    [InlineKeyboardButton(text='Взносы', callback_data='tax')],

])



reply_keyboard = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text='Регистрация', callback_data='register'), 
        KeyboardButton(text='Вакансии', callback_data='vacancy'), 
        KeyboardButton(text='О нас', callback_data='about')
        ]],
    resize_keyboard=True,
    input_field_placeholder='Пожалуйста, зарегистрируйтесь'
)