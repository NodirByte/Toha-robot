from aiogram import types
from handlers.channels.user_channels import check_user_is_member
from loader import dp
from keyboards.inline.channel_inline import get_channel_inline_button
from utils.db_api.connector_db import get_or_create_user
from keyboards.default.user_keyboards import get_category_keyboard, get_tests_menu_keyboard
from keyboards.default.user_keyboards import get_course_lessons_menu_keyboard

@dp.message_handler(text="🏠 Bosh sahifa")
async def bot_start(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    print("Member on start:", member)
    user, created = await get_or_create_user(telegram_id)
    category_keyboard = get_category_keyboard()
    if member:
        await message.answer("Assalomu alaykum! Ushbu botga xush kelibsiz!", reply_markup=category_keyboard)
    else:
        await message.answer("Assalomu alaykum! Ushbu botga xush kelibsiz! Botdan foydalanish uchun kanalimizga a'zo bo'ling:", reply_markup=get_channel_inline_button())

@dp.message_handler(text="📚 Bepul Darslar")
async def free_lessons_menu(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    if not member:
        await message.answer("Darslardan foydalanish uchun avval kanalimizga a'zo bo'ling:", reply_markup=get_channel_inline_button())
        return
    await message.answer(f"Darslar bo'limi:\nSiz ushbu kanal orqali arab tili kurslaridan foydalanishingiz mumkin https://t.me/muftillayevluqmonjon")

@dp.message_handler(text="🎞 Arab tili kurslari")
async def courses_lesson_menu(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    if not member:
        await message.answer("Kurslardan foydalanish uchun avval kanalimizga a'zo bo'ling:", reply_markup=get_channel_inline_button())
        return
    course_lessons_menu_keyboard = get_course_lessons_menu_keyboard()
    await message.answer("Kurslar bo'limi", reply_markup=course_lessons_menu_keyboard)

@dp.message_handler(text="📊 Natijalar")
async def results_menu(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    if not member:
        await message.answer("Natijalardan foydalanish uchun avval kanalimizga a'zo bo'ling:", reply_markup=get_channel_inline_button())
        return
    await message.answer("Natijalar bilish uchun kerakli kanalimiz: https://t.me/https://t.me/LuqmonjonMuftillayev")

@dp.message_handler(text="📞 Aloqa")
async def contact_us(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    category_keyboard = get_category_keyboard()
    channel_inline_button = get_channel_inline_button()
    if not member:
        await message.answer("Biz bilan aloqa uchun avval kanalimizga a'zo bo'ling:", reply_markup=channel_inline_button)
        return
    await message.answer("Biz bilan aloqa bo'limi", reply_markup=channel_inline_button)

@dp.message_handler(text="👤 Luqmonjon Muftillayev kim?")
async def who_is_luqmonjon(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    if not member:
        await message.answer("Ushbu bo'limdan foydalanish uchun avval kanalimizga a'zo bo'ling:", reply_markup=get_channel_inline_button())
        return
    await message.answer("Luqmonjon Muftillayev kim?\n\nLuqmonjon Muftillayev - arab tili o'qituvchi, tarjimon va mutarjimdir. Uning kanalida siz arab tili kurslaridan foydalanishingiz mumkin. Kanalga a'zo bo'lib, kurslar va darslar haqida ma'lumot olishingiz mumkin: https://t.me/LuqmonjonMuftillayev")
