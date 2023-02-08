from aiogram import types
from loader import dp
from data.config import ADMINS
#from filters import IsPrivate

@dp.message_handler(state=None, user_id=ADMINS, commands="post")
async def post(message: types.Message):
	await message.answer("Siz adminsiz")
