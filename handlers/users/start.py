from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from handlers.channels.user_channels import check_user_is_member
from loader import dp
from keyboards.inline.channel_inline import get_channel_inline_button
from utils.db_api.connector_db import get_or_create_user
from keyboards.default.user_keyboards import get_category_keyboard


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    user, created = await get_or_create_user(telegram_id)
    if member:
        await message.answer(f"Assalomu alaykum {message.from_user.first_name}! Ushbu botga xush kelibsiz!", reply_markup=get_category_keyboard())
    else:
        await message.answer(f"Assalomu alaykum {message.from_user.first_name}! Ushbu botga xush kelibsiz! Botdan foydalanish uchun kanalimizga a'zo bo'ling:", reply_markup=get_channel_inline_button())
    

@dp.callback_query_handler(text="refresh:bot")
async def refresh_channel_inline(call: types.CallbackQuery):
    telegram_id = call.from_user.id
    member = await check_user_is_member(telegram_id)
    if member:
        await call.message.answer("Siz kanalimizga a'zo bo'lgansiz!", reply_markup=get_category_keyboard())
    else:
        await call.message.answer("Kanalimizga a'zo bo'ling!", reply_markup=get_channel_inline_button())