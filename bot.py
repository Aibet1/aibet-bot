from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import logging

API_TOKEN = '7785774749:AAEhwdkeT4aZJGRvC00n1bLPEjxvj4u0lY'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text='Premium - 3 days / 3 bets', url='https://t.me/send?start=IVIEvkzuuWf5'),
        InlineKeyboardButton(text='Premium+ - 7 days / 10 bets', url='https://t.me/send?start=IVyn2pBmkjwA'),
        InlineKeyboardButton(text='VIP - 30 days / 40 bets', url='https://t.me/send?start=IVdL5v6alzvN'),
        InlineKeyboardButton(text='VIP+ - 3 months / 100+ bets', url='https://t.me/send?start=IVfSZwBBISRX'),
        InlineKeyboardButton(text='Super VIP - 12 months / 500+ bets', url='https://t.me/send?start=IVjalA79rCA4'),
    )
    await message.answer("Choose your subscription plan:", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
