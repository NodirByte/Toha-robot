from aiogram import types
from data.excel_function import export_user_data_to_excel
from handlers.channels.user_channels import check_user_is_member
from loader import dp, bot
from keyboards.inline.channel_inline import get_admin_inline_button, get_channel_inline_button, get_free_lessons_inline_button
from states.user_states import CourseState, SearchState
from utils.db_api.connector_db import (
    get_admin_description,
    get_all_courses,
    get_course_lessons,
    get_exam_results,
    get_gift,
    get_or_create_user,
    get_lesson_by_title,
)
from keyboards.default.user_keyboards import (
    get_category_keyboard,
    get_tests_menu_keyboard,
)
from keyboards.default.user_keyboards import get_course_lessons_menu_keyboard
from django.core.exceptions import ObjectDoesNotExist
from aiogram.dispatcher import FSMContext
from aiogram.utils import exceptions


@dp.message_handler(text="🏠 Bosh sahifa")
async def bot_start(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    user, created = await get_or_create_user(telegram_id)
    category_keyboard = get_category_keyboard()
    if member:
        await message.answer(
            "Assalomu alaykum! Ushbu botga xush kelibsiz!",
            reply_markup=category_keyboard,
        )
    else:
        await message.answer(
            "Assalomu alaykum! Ushbu botga xush kelibsiz! Botdan foydalanish uchun kanalimizga a'zo bo'ling:",
            reply_markup=get_channel_inline_button(),
        )


@dp.message_handler(text="📚 Bepul Darslar")
async def free_lessons_menu(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    free_lessons_inline_button = await get_free_lessons_inline_button()
    if not member:
        await message.answer(
            "Darslardan foydalanish uchun avval kanalimizga a'zo bo'ling:",
            reply_markup=get_channel_inline_button(),
        )
        return
    await message.answer(
        f"Darslar bo'limi:\nSiz ushbu kanal orqali arab tili kurslaridan foydalanishingiz mumkin",
        reply_markup=free_lessons_inline_button,
    )


@dp.message_handler(text="🎞 Arab tili kurslari", state=None)
async def courses_lesson_menu(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    if not member:
        await message.answer(
            "Kurslardan foydalanish uchun avval kanalimizga a'zo bo'ling:",
            reply_markup=get_channel_inline_button(),
        )
        return
    course_lessons_menu_keyboard = await get_course_lessons_menu_keyboard()
    await message.answer("Kurslar bo'limi", reply_markup=course_lessons_menu_keyboard)
    await CourseState.course.set()


@dp.message_handler(state=CourseState.course)
async def course_lessons(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    courses = await get_course_lessons_menu_keyboard()
    if not member:
        await message.answer(
            "Kurslardan foydalanish uchun avval kanalimizga a'zo bo'ling:",
            reply_markup=get_channel_inline_button(),
        )
        await state.finish()
        return
    course_title = message.text.strip()
    if course_title == "🏠 Bosh sahifa":
        await message.answer(
            "Bosh sahifaga qaytildi", reply_markup=get_category_keyboard()
        )
        await state.finish()
        return
    all_courses = await get_all_courses()   
    if any(course == course_title for course in all_courses): 
        await message.answer(
            "Kursni berilgan nomi bilan topa olmadik. Iltimos, qayta urinib ko'ring.",
            reply_markup=get_category_keyboard(),
        )
        await state.finish()
        return
    lessons = await get_course_lessons(course_title)
    if not lessons:
        await message.answer(
            "Kursda darslar topilmadi. Iltimos, boshqa kurs tanlang.",
            reply_markup=courses,
        )
        await CourseState.course.set()
        return
    try:
        for lesson in lessons:
            lesson_title = lesson.title
            lesson_path = lesson.lesson.path
            with open(lesson_path, "rb") as file:
                await message.bot.send_document(
                    telegram_id, file, caption=lesson_title, reply_markup=get_category_keyboard()
                )
        await state.finish()
    except Exception as e:
        print(f"Error sending document: {e}")
        await message.answer(
            "Xatolik sodir bo'ldi. Iltimos, keyinroq urinib ko'ring.",
            reply_markup=get_category_keyboard(),
        )
    await state.finish()


@dp.message_handler(text="🔍 Qidirish", state=None)
async def search_menu(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    if not member:
        await message.answer(
            "Qidirish tugmasidan foydalanish uchun avval kanalimizga a'zo bo'ling:",
            reply_markup=get_channel_inline_button(),
        )
        return
    await message.answer(
        "Kerakli bo'lgan dars nomini kiriting:",
        reply_markup=types.ReplyKeyboardRemove(),
    )
    await SearchState.search.set()


@dp.message_handler(state=SearchState.search)
async def search_lesson(message: types.Message, state: FSMContext):
    lesson_title = message.text
    category_keyboard = get_category_keyboard()
    telegram_id = message.from_user.id

    # Search for the lesson in the database
    try:
        lesson = await get_lesson_by_title(lesson_title)
    except ObjectDoesNotExist:
        await message.answer(
            "Ushbu nomli dars topilmadi", reply_markup=category_keyboard
        )
        await state.finish()
        return

    # If lesson found, send the lesson file to the user
    if lesson.lesson:
        try:
            lesson_path = (
                lesson.lesson.path
            )  # Assuming lesson.lesson is FileField in Django
            lesson_title = lesson.title
            with open(lesson_path, "rb") as file:
                await message.bot.send_document(
                    telegram_id,
                    file,
                    caption=lesson_title,
                    reply_markup=category_keyboard,
                )
        except Exception as e:
            print(f"Error sending document: {e}")
            await message.answer(
                "Xatolik sodir bo'ldi. Iltimos, keyinroq urinib ko'ring.",
                reply_markup=category_keyboard,
            )

        # Reset the state to `None` after handling the lesson search
        await state.finish()
    else:
        await message.answer(
            "Darsning fayli topilmadi. Iltimos, qayta urinib ko'ring.",
            reply_markup=category_keyboard,
        )
        await state.finish()
        return


@dp.message_handler(text="📊 Cefr va At Tanal natijalar")
async def results_menu(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    if not member:
        await message.answer(
            "Natijalardan foydalanish uchun avval kanalimizga a'zo bo'ling:",
            reply_markup=get_channel_inline_button(),
        )
        return
    results = await get_exam_results() 
    try:
        for result in results:
            result_text = result.text
            result_path = result.exam_file.path
            with open(result_path, "rb") as file:
                await message.bot.send_document(
                    telegram_id, file, caption=result_text, reply_markup=get_category_keyboard()
                )
    except Exception as e:
        print(f"Error sending document: {e}")
        await message.answer(
            "Xatolik sodir bo'ldi. Iltimos, keyinroq urinib ko'ring.",
            reply_markup=get_category_keyboard(),
        )
    


@dp.message_handler(text="📞 Aloqa")
async def contact_us(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    admin_inline_button = await get_admin_inline_button()
    channel_inline_button = get_channel_inline_button()
    if not member:
        await message.answer(
            "Biz bilan aloqa uchun avval kanalimizga a'zo bo'ling:",
            reply_markup=channel_inline_button,
        )
        return
    await message.answer("Biz bilan aloqa bo'limi", reply_markup=admin_inline_button)


@dp.message_handler(text="🎁 Gift")
async def gift_menu(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    category_keyboard = get_category_keyboard()

    if not member:
        await message.answer(
            "Sovg'ani olish uchun avval kanalimizga a'zo bo'ling:",
            reply_markup=get_channel_inline_button(),
        )
        return

    gift = await get_gift()
    if gift and gift.gift:  # Check if gift and gift.gift exist
        file_path = gift.gift.path  # Get the file path in the local filesystem

        caption = gift.title
        try:
            with open(file_path, "rb") as file:
                await message.bot.send_document(
                    telegram_id, file, caption=caption, reply_markup=category_keyboard
                )
        except Exception as e:
            print(f"Error sending document: {e}")
            await message.answer(
                "Xatolik sodir bo'ldi. Iltimos, keyinroq urinib ko'ring.",
                reply_markup=category_keyboard,
            )
    else:
        await message.answer(
            "Hozircha hech qanday gift topilmadi. Iltimos, keyinroq urinib ko'ring.",
            reply_markup=category_keyboard,
        )


@dp.message_handler(text="👤 Luqmonjon Muftillayev kim?")
async def who_is_luqmonjon(message: types.Message):
    telegram_id = message.from_user.id
    member = await check_user_is_member(telegram_id)
    if not member:
        await message.answer(
            "Ushbu bo'limdan foydalanish uchun avval kanalimizga a'zo bo'ling:",
            reply_markup=get_channel_inline_button(),
        )
        return
    admin_info = await get_admin_description()
    await message.answer(
        admin_info
    )


@dp.message_handler(text=":$-Download-$:")
async def download_xlsx(message: types.Message):
    telegram_id = message.from_user.id
    students_xlsx = await export_user_data_to_excel()
    print("Exel file path: - > ", students_xlsx)
    await bot.send_document(chat_id=telegram_id, document=open(students_xlsx, "rb"))
