import sys
from dataclasses import dataclass
from environs import Env

# Описываем структуру с данными о Telegram-боте
@dataclass
class TgBot:
    token: str   # Токен доступа к боту
    admin_id: int    # ID администратора бота

@dataclass
class Config:
    tg_bot: TgBot    # Настройки бота (в будущем можно добавить другие секции конфигурации)

def load_config():
    env = Env()
    try:
        env.read_env()
        return Config(
            tg_bot=TgBot(
                token=env.str("BOT_TOKEN"),
                admin_id=env.int("ADMIN_ID")
            )
        )
    except Exception as e:
        print(f"Ошибка загрузки конфига: {e}")
        sys.exit(1)

