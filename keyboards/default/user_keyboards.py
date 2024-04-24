from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from utils.db_api.connector_db import get_all_courses

def get_category_keyboard():
    category_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="👤 Luqmonjon Muftillayev kim?"),
            ],
            [
                KeyboardButton(text="📚 Bepul Darslar"), 
                KeyboardButton(text="🔍 Qidirish"),
                KeyboardButton(text="🎞 Arab tili kurslari")
            ],
            [
                KeyboardButton(text="📊 Cefr va At Tanal natijalar"),
                KeyboardButton(text="📞 Aloqa"),
            ],
            [
                KeyboardButton(text="🎁 Gift"),
            ],
        ],
        resize_keyboard=True
    )
    return category_keyboard

async def get_course_lessons_menu_keyboard():
    lessons = await get_all_courses()

    # Initialize an empty list to store row lists of buttons
    rows = []

    # Create rows of buttons with a maximum of two buttons per row
    current_row = []
    for lesson in lessons:
        current_row.append(KeyboardButton(text=lesson.title))
        # Check if the current_row has reached the maximum size (2 buttons per row)
        if len(current_row) == 2:
            rows.append(current_row)
            current_row = []  # Reset the current_row for the next row

    # Add any remaining buttons if the number of lessons is odd
    if current_row:
        rows.append(current_row)

    # Add a "🏠 Bosh sahifa" button as the last row
    rows.append([KeyboardButton(text="🏠 Bosh sahifa")])

    # Construct the ReplyKeyboardMarkup with the rows of buttons
    lessons_menu_keyboard = ReplyKeyboardMarkup(
        keyboard=rows,
        resize_keyboard=True
    )

    return lessons_menu_keyboard



def get_tests_menu_keyboard():
    tests_menu_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🇸🇦 Arab tili testlari"),
                KeyboardButton(text="🇸🇦 Arab tili topshiriqlari")
            ],
            [
                KeyboardButton(text="🏠 Bosh sahifa"),
            ]
        ],
        resize_keyboard=True
    )
    return tests_menu_keyboard


def get_home_keyboard():
    home_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🏠 Bosh sahifa"),
            ]
        ],
        resize_keyboard=True
    )
    return home_keyboard



# async def get_lesson_by_title_keyboard(lesson_name: str) -> ReplyKeyboardMarkup:
#     lessons = await get_all_courses()
#     lesson = None
#     for l in lessons:
#         if l.title == lesson_name:
#             lesson = l
#             break

#     if lesson is None:
#         return None

#     lessons_menu_keyboard = ReplyKeyboardMarkup(
#         keyboard=[
#             [
#                 KeyboardButton(text=lesson.title),
#             ],
#             [
#                 KeyboardButton(text="🏠 Bosh sahifa"),
#             ]
#         ],
#         resize_keyboard=True
#     )

#     return lessons_menu_keyboard
