import random
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7767847250:AAGW_8XhdIA2JRfYIw6RAyTMrGOt4v2iPuY"
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Функция для создания клавиатуры
def get_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Найти информацию', callback_data='find_info')],
            [InlineKeyboardButton(text='Связь', callback_data='contact')],
            [InlineKeyboardButton(text='О боте', callback_data='about')]
        ]
    )

# Обработчик команды /start
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Это тестовый бот",
        reply_markup=get_keyboard()
    )


@dp.message(Command("help"))
async def help_command(message: types.Message):
    command_text=(
        'Доступные команды:\n'
        '/start - Начать работу с ботом\n'
        '/help - Показывает список команд\n'
        '/random - Случайное число'
    )
    await message.answer(command_text)

@dp.message(Command("random"))
async def random_command(message: types.Message):  # Исправлено
    number = random.randint(1, 100)
    await message.answer(f"Случайное число: {number}")


# Обработчик callback-кнопок
@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data == "find_info":
        await callback.message.answer("Введите информацию для поиска")
    elif callback.data == "contact":
        await callback.message.answer("Напишите нам в личку: @")
    elif callback.data == "about":
        await callback.message.answer("Это бот, написанный на библиотеке Aiogram.")

    await callback.answer()

# Запуск бота
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())  # Использовать ТОЛЬКО в обычных скриптах, не в Jupyter/IDE




