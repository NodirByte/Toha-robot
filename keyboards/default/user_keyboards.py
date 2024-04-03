from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_category_keyboard():
    category_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="👤 Luqmonjon Muftillayev kim?"),
            ],
            [
                KeyboardButton(text="📚 Bepul Darslar"), 
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

def get_course_lessons_menu_keyboard():
    # saudi arabia tili darslari
    lessons_menu_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🇸🇦 Boshlang’ich A1-A2"),
                KeyboardButton(text="🇸🇦 At Tanal")
            ],
            [
                KeyboardButton(text="🇸🇦 Cefr intensiv 1 oylik"),
                KeyboardButton(text="🇸🇦 Nahv+e’rob+mutolaa"),
            ],
            [
                KeyboardButton(text="🇸🇦 Yuqori Nahv"),
                KeyboardButton(text="🇸🇦 Cefr Classic 4 oy"),
            ],
            [
                KeyboardButton(text="🇸🇦 Sinxron tarjimonlik"),
                KeyboardButton(text="🇸🇦 Mutolaa"),
                KeyboardButton(text="🇸🇦 Amaliy Sarf"),
            ],
            [
                KeyboardButton(text="🏠 Bosh sahifa"),
            ]
        ],
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
