from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import token, admins

#Connect к боту#
storage=MemoryStorage()
bot=Bot(token)
dp=Dispatcher(bot, storage=storage)
admins=admins