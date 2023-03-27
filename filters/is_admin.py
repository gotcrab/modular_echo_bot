from aiogram.types import Message
from config_data.config import Config, load_config

config: Config = load_config()


def is_admin(message: Message):
    return message.from_user.id in config.tg_bot.admin_ids
