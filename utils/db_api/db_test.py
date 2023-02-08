from db_gino import db
import quick_commands as commands
import config
import asyncio


async def db_test():
	await db.set_bind(config.POSTGRES_URI)
	await db.gino.drop_all()
	await db.gino.create_all()

	users = await commands.select_all_users()
	print(users)

	count = await commands.count_users()
	print(count)

	user = await commands.select_user(1)
	print(user)

	await commands.update_user_name(1, "Yangilangan ism")


loop = asyncio.get_event_loop()
loop.run_until_complete(db_test())