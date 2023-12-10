import asyncio
import logging
import time
"""from dotenv import load_dotenv 
   Эта хуйня короче позволяет скрыть токен при загрузке в общий доступ и я подумал, что нам это в копилку засчитают но сука по одномой только богам извстной причине эта залупа не работает """
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import os

logging.basicConfig(level=logging.INFO)


bot = Bot("5583219536:AAHTatrkaiGyursYDykLSAwwTUSDi8Lcr2c")

dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")

@dp.message(Command("info"))
async def cmd_start(message: types.Message):
    await message.answer("Что он может? Да нихуя собственно")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
