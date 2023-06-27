from command_handlers import dp
from states import dp
from aiogram.utils import executor


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)
