import telegram
import os
import asyncio
from configparser import ConfigParser

config_dir = os.path.normpath(os.getenv("CONFIG_PATH", f"{os.getcwd()}/config"))
config = ConfigParser()
config_file = os.path.normpath(f"{config_dir}/config.ini")
if os.path.isfile(config_file):
    config.read(config_file)
else:
    config.add_section("telegram")
    config.set("telegram", "chatid", "")
    config.set("telegram", "tokenid", "")




message = "geny is a stupid nerd2"



bot = telegram.Bot(token=config.get("telegram","tokenid"))
asyncio.run(bot.send_message(chat_id=config.get("telegram","chatid"), text=message))

