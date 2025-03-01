"""
The most simple echo bot implemented with aiogram framework
"""

import asyncio
import logging

from aiogram import Bot, Dispatcher, F, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import settings

bot = Bot(token=settings.bot.token)
dp = Dispatcher()

router = Router(name="sd")


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        text=settings.text.start_text,
        parse_mode="HTML",
    )


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(text=settings.const.help_text, parse_mode="HTML")


@dp.message(F.text == "d")
async def listen_message_d(message: types.Message):
    await message.answer(text="ddd")


@dp.message(F)
async def listen_message(message: types.Message):
    builder = InlineKeyboardBuilder()
    buttons = [
        types.InlineKeyboardButton(text="В ВЕРХНИЙ РЕГИСТР", callback_data="uppercase"),
        types.InlineKeyboardButton(text="в нижний регистр", callback_data="lowercase"),
        types.InlineKeyboardButton(text="Развернуть текст", callback_data="reverse"),
    ]
    builder.row(*buttons)

    await message.answer(text=message.text, reply_markup=builder.as_markup())


@dp.callback_query(F.data == "uppercase")
async def uppercase(callback: types.CallbackQuery):
    user_text = callback.message.text.upper()

    if user_text != callback.message.text:  # Проверяем, изменился ли текст
        await callback.message.edit_text(text=user_text, reply_markup=None)
    else:
        await callback.answer(
            "Текст уже в верхнем регистре!", show_alert=True
        )  # Сообщение пользователю


@dp.callback_query(F.data == "lowercase")
async def lowercase(callback: types.CallbackQuery):
    user_text = callback.message.text.lower()
    if user_text != callback.message.text:
        await callback.message.edit_text(text=user_text, reply_markup=None)
    else:
        await callback.answer(
            "Текст уже в нижнем регистре!", show_alert=True
        )  # Сообщение пользователю


@dp.callback_query(F.data == "reverse")
async def reverse(callback: types.CallbackQuery):
    user_text = "".join(reversed(callback.message.text))
    await callback.message.edit_text(text=user_text, reply_markup=None)


# ---------------------------------------------------------------------------- #
#                                 running func                                 #
# ---------------------------------------------------------------------------- #


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stopped by user.")
