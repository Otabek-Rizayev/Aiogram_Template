from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from filters import IsPrivate
from utils.misc import rate_limit
from utils.db_api import quick_commands as commands

@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), commands="start")
async def start_base(message: types.Message):
    await message.answer("salom!")
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == "active":
            await message.answer(f"Salom! {user.full_name}",
                                 f"Siz bazaga kiritilgansiz!")
        elif user.status == "banned":
            await message.answer("Siz botdan foydalana olmaysiz!")
    except Exception:
        await commands.add_user(
                user_id=message.from_user.id,
                full_name=message.from_user.full_name,
                username=message.from_user.username,
                status='active')
        await message.answer("Siz ro'yxatga olindingiz!")

@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), commands="ban")
async def get_ban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status="banned")
    await message.answer("Siz ban oldingiz")

@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), commands="unban")
async def get_unban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status="active")
    await message.answer("Siz bandan chiqdingiz!")

@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), commands="profile")
async def get_info(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    await message.answer(f"ID - {user.user_id}\n"
                         f"Ism - {user.full_name}\n"
                         f"Username - {user.username}\n"
                         f"Status - {user.status}")


