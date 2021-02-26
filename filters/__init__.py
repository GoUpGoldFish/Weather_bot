from aiogram import Dispatcher
from .private_chat import IsPrivate

# from .is_admin import AdminFilter

def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)

#
# if __name__ == "filters":
#     #dp.filters_factory.bind(is_admin)
#     pass
