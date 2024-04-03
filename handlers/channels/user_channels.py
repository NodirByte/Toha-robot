from aiogram import types
from loader import dp, bot

# CHANNEL_ID = "-1001995533451" # Channel ID TEST
CHANNEL_ID = "-1001673432975" # Channel ID

async def check_user_is_member(user_id: int):
    try:
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=user_id)
        if member.status == "member" or member.status == "administrator" or member.status == "creator":
            return True
        else:
            return False
    except Exception as e:
        return None
        