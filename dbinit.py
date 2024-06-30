import sqlite3
import datetime
import os

dbname = "bosstimer.db"

def initialize_db():
    #delete the existing db to make from scratch
    if os.path.exists(dbname):
        os.remove("bosstimer.db")
    else:
        pass
    sql_statements = """CREATE TABLE IF NOT EXISTS bosstimer (
                time text PRIMARY KEY, 
                happened boolean
        )"""
    try:
        with sqlite3.connect(dbname) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_statements)
            conn.commit()
    except sqlite3.Error as e:
        print(e)
    #initialize last known good time of a boss spawn as anchor point. TODO: make this come from docker env.
    bosstime = datetime.datetime(2024, 6, 26, 0, 0, 0)
    #initialize the next 6000 boss timers, cause fuck it.
    for i in range(6000):
        timeincrement = datetime.timedelta(minutes=210)
        bosstime = bosstime + timeincrement
        try:
            cursor.execute("Insert into bosstimer (time,happened) values (?,?)",(bosstime, False))
        except sqlite3.Error as e:
            print(e)
    try:
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def past():
    #this is to change a flag for every boss event to see if it's in the past or future. Since the anchor point is static, this needs to happen.
    try:
        with sqlite3.connect(dbname) as conn:
            cursor = conn.cursor()
            cursor.execute("update bosstimer set happened = 1 where time <= strftime('%Y-%m-%d %H:%M:%S', datetime('now', 'localtime'))")
    except sqlite3.Error as e:
        print(e)

