from .schemas.user import User
from asyncpg import UniqueViolationError
from .db_gino import db

async def add_user(user_id: int, full_name: str, username: str, status: str):
	try:
		user = User(user_id=user_id, full_name=full_name, username=username, status=status)
		await user.create()
	except UniqueViolationError:
		print("Foydalanuvchi qo'shilmadi!")

async def select_all_users():
	users = await User.query.gino.all()
	return users

async def count_users():
	count = await db.func.count(User.user_id).gino.scalar()
	return count

async def select_user(user_id):
	user = await User.query.where(User.user_id == user_id).gino.first()
	return user

async def update_status(user_id, status):
	user = await select_user(user_id)
	await user.update(status=status).apply()