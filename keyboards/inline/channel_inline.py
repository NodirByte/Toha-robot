from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.db_api.connector_db import get_channel_link, get_admin1, get_admin2, get_admin_description

def get_channel_inline_button():
    channel_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            # InlineKeyboardButton(text="A'zo bo'ling", url="https://t.me/DevTestChannel1")
            InlineKeyboardButton(text="Aloqa uchun!", url="https://t.me/muftillayevluqmonjon")
        ],
        [
            # InlineKeyboardButton(text="🔄 Refresh", callback_data="refresh:bot")
        ],
    ]
    )
    return channel_inline_button

async def get_admin_inline_button():
    admin1 = await get_admin1()
    admin2 = await get_admin2()
    
    admin_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📢 Kanalga o'tish", url="https://t.me/muftillayevluqmonjon")
        ],
        [
            InlineKeyboardButton(text="📞 Admin 1", url=admin1),
            InlineKeyboardButton(text="📞 Admin 2", url=admin2)
        ],
    ]
    )
    return admin_inline_button

async def get_free_lessons_inline_button():
    channel_link = await get_channel_link()
    free_lessons_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📢 Kanalga o'tish uchun quydagi link ustiga bosing!", url=channel_link)
        ],
    ]
    )
    return free_lessons_inline_button