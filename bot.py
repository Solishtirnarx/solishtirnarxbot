import os
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(types.CommandStart())
async def start(message: types.Message):
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "Bu — Solishtirnarxbot 🤖\n"
        "Mahsulot nomini yuboring, men narxlarni solishtirib beraman.\n\n"
        "Til: O‘zbek 🇺🇿 / Русский 🇷🇺"
    )

async def main():
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
