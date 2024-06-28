import telegram
import os
import asyncio
import schedule
import time
from configparser import ConfigParser
from dbinit import *

config_dir = os.path.normpath(os.getenv("CONFIG_PATH", f"{os.getcwd()}/config"))
config = ConfigParser()
config_file = os.path.normpath(f"{config_dir}/config.ini")
if os.path.isfile(config_file):
    config.read(config_file)
else:
    config.add_section("telegram")
    config.set("telegram", "chatid", "")
    config.set("telegram", "tokenid", "")



def message():
    print("fag")




def checktime():
    bosstime = nexttime(dbname)
    print(bosstime)

schedule.every(3).seconds.do(checktime)


#print(schedule)
while True:
   schedule.run_pending()
   time.sleep(1)



#bot = telegram.Bot(token=config.get("telegram","tokenid"))
#asyncio.run(bot.send_message(chat_id=config.get("telegram","chatid"), text=message))

