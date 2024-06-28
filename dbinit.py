import sqlite3
import datetime

dbname = "bosstimer.db"



def create_sqlite_database(filename):
    """ create a database connection to an SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(filename)
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


def initialize_db(filename):

    sql_statements = """CREATE TABLE IF NOT EXISTS bosstimer (
                time text PRIMARY KEY, 
                happened boolean
        )"""
    try:
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()
            cursor.execute(sql_statements)
            conn.commit()
    except sqlite3.Error as e:
        print(e)

    #see if the table has been filled already. If not, fill it!
    cursor.execute("select * from bosstimer")
    rows = len(cursor.fetchall())

    bosstime = datetime.datetime(2024, 6, 26, 0, 0, 0)
    if rows == 0:               
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
    else:
        print("Rows already initialized!")

def past(filename):
    try:
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()

            cursor.execute("update bosstimer set happened = 1 where time <= strftime('%Y-%m-%d %H:%M:%S', datetime('now', 'localtime'))")
    except sqlite3.Error as e:
        print(e)

def nexttime(filename):
    try:
        with sqlite3.connect(filename) as conn:
            cursor = conn.cursor()

            cursor.execute("select time from bosstimer where happened = 0 limit 1")
            time = cursor.fetchone()[0]
            time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
    
            return time

    except sqlite3.Error as e:
        print(e)


if __name__ == '__main__':
    create_sqlite_database(dbname)
    initialize_db(dbname)
    past(dbname)
    nexttime(dbname)

