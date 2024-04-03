from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_channel_inline_button():
    channel_inline_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            # InlineKeyboardButton(text="A'zo bo'ling", url="https://t.me/DevTestChannel1")
            InlineKeyboardButton(text="A'zo bo'ling", url="https://t.me/muftillayevluqmonjon")
        ],
        [
            # InlineKeyboardButton(text="🔄 Refresh", callback_data="refresh:bot")
        ],
    ]
    )
    return channel_inline_button
