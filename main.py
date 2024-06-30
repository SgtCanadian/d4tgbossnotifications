import telegram
import os
import asyncio
import schedule
import time
import datetime
from configparser import ConfigParser
from dbinit import *
from apscheduler.schedulers.background import BlockingScheduler


#initialize the db from dbinit.py
initialize_db()

sched = BlockingScheduler()
advancewarning = datetime.timedelta(minutes=15)
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
    print("nerd")
    bot = telegram.Bot(token=config.get("telegram","tokenid"))
    asyncio.run(bot.send_message(chat_id=config.get("telegram","chatid"), text="15 Minute Warning"))
    

with sqlite3.connect(dbname) as conn:
    cursor = conn.cursor()
    past()
    cursor.execute("select time from bosstimer where happened = 0")
    cursor.row_factory = None
    rows = cursor.fetchall()
    for row in rows:
        bosstime = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
        if bosstime.weekday() >= 0 and bosstime.weekday() <= 4:
            if bosstime.hour >= 6 and bosstime.hour <= 22:
                sched.add_job(message, 'date', run_date = bosstime)
            else:
                pass
        else:
            if bosstime.hour >= 8 and bosstime.hour <= 23:
                sched.add_job(message, 'date', run_date = bosstime)
            else:
                pass
sched.start()






