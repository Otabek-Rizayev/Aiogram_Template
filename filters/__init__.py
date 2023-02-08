#from aiogram import Dispatcher
from .private_chat import IsPrivate
from loader import dp
# from .is_admin import AdminFilter


# def setup(dp: Dispatcher):
#     dp.filters_factory.bind(IsPrivate)

if __name__ == "filters":
    dp.filters_factory.bind(IsPrivate)
    pass
