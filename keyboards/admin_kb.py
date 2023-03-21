from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

# загрузка футболки
download_merch_kb = ReplyKeyboardMarkup(resize_keyboard=True) # первая клавиатура админа
download_merch_btn = KeyboardButton('/Загрузить_мерч')
download_merch_kb.add(download_merch_btn)

