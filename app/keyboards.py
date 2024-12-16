from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Привет')]
],
                        resize_keyboard=True,
                        input_field_placeholder='Выберите команду...')