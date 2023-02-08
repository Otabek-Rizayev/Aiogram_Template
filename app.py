from aiogram import executor
from loader import dp, db
import middlewares, filters, handlers
from utils.db_api.db_gino import on_startup_base
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    # filters.setup(dp)
    print("postgresql ishga tushdi!")
    await on_startup_base(dp)

    print("baza o'chirirldi!")
    await db.gino.drop_all()

    print("Baza yaratildi!")
    await db.gino.create_all()

    # Birlamchi komandalar (/star va /help)
    await set_default_commands(dp)

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
