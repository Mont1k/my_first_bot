from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PROXY_URL = "http://proxy.server:3128"
storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
DESTINATION = '/Users/user/PycharmProjects/geek_34_1_bot/'
