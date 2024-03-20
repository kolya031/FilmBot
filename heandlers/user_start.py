from loader import dp, bot
from aiogram import types
from aiogram.dispatcher.filters import CommandStart, CommandHelp
from data.db import add_user, get_text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#комманда /start#
@dp.message_handler(CommandStart())
async def cmd_start(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        try:
            await add_user(user_id=message.from_user.id, user_menotion=message.from_user.id)
        except:
            pass
        text_start=await get_text(type='text_text', text_type='wellcome')
        text_start=text_start[0][0]
        me=await bot.get_me()
        text_start=str(text_start).replace('{username_bot}', me.mention)
        text_start=str(text_start).replace('{bot_id}', str(me.id))
        text_start=str(text_start).replace('{username}', message.from_user.mention)
        text_start=str(text_start).replace('{full_name}', message.from_user.full_name)
        text_start=str(text_start).replace('{user_id}', str(message.from_user.id)) 
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton("🚀 Популярное"))
        keyboard.add(KeyboardButton("🔍 Поиск"))
        keyboard.add(KeyboardButton("💬 Контакты"))
        await message.answer(text=text_start, reply_markup=keyboard, parse_mode=types.ParseMode.MARKDOWN)