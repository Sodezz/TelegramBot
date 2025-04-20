import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from typing import Optional
from configs.config import config
from colorlog import ColoredFormatter

# Настраиваем базовый логгер для вывода информации в консоль
logger = logging.getLogger()
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = ColoredFormatter(
    fmt="{log_color}Время: {asctime}\n{levelname}: {message}\n",
    datefmt="%m-%d %H:%M:%S",
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "bold_red"
    },
    style="{"
)

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Создаем объекты бота и диспетчера и загружаем переменные окружения из файла config.py
bot: Bot = Bot(token=config.API_TOKEN.get_secret_value())
dp: Dispatcher = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message) -> None:
    """
    Хэндлер команды /start.

    Отправляет приветственное сообщение пользователю.
    """
    user_first_name: Optional[str] =  message.from_user.first_name or "Пользователь"
    await message.answer(f"Hello, {user_first_name}!")

async def main():
    """
    Точка входа: запускает процесс получения и обработки обновлений от Telegram (polling).
    """
    logging.info("Бот запущен в polling режиме")
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запускаем event loop и запускаем бота
    asyncio.run(main())