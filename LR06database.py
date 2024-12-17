import sqlite3
import datetime
from mylib import dt


def openDB():
    # Создаем подключение к базе данных (файл my_database.db будет создан)
    connection = sqlite3.connect('my_database.db')

    #print('подключение к БД')

    return connection


def closeDB(pconnection):
    if pconnection is not None:
        pconnection.commit()
        pconnection.close()
    #print('отключение от БД')
    return True


def printTable(pTable):
    if len(pTable) == 0: return False
    try:
        connection = openDB()
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {pTable}")
        xcolumns = [column[0] for column in cursor.description]
        #print(list((cursor.description)))
        print(xcolumns)
        data = cursor.fetchall()
        #print(data)

        for row in data:
            for i in range(len(row)):
                print(xcolumns[i],' * ', row[i])
            print('\n')

    except Exception as e:
        print('ошибка с БД', e)
    finally:
        cursor.close()
        closeDB(connection)

def initTableLR06(pTable):
    print('инициализация...')
    try:
        if 0 == len(pTable): pTable = 'special_date'

        connection = openDB()
        cursor = connection.cursor()


        cursor.execute(f"PRAGMA page_size = 512")
        cursor.execute(f"PRAGMA encoding = 'UTF-8'")

        cursor.execute(f"DROP TABLE IF EXISTS {pTable}")
        cursor.execute(f"DROP INDEX IF EXISTS {pTable}_idx_age")
        cursor.execute("VACUUM")

        print('удалили таблицу/индекс')

        sql = f"""
        CREATE TABLE IF NOT EXISTS {pTable} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            datetime integer not null,
            type INTEGER, 
            description TEXT
            
        )
        """
        cursor.execute(sql)
        print('создали таблицу')

        #cursor.execute(f'CREATE INDEX {pTable}_idx_age ON {pTable} (age)')
        #print('создали индекс')

        # данные для добавления
        zap = (dt("2024-11-04 0:0:0"), 0,"День народного единства")
        cursor.execute(f"INSERT INTO {pTable} (datetime,type, description) VALUES (?, ?, ?)", zap)
        print('добавили ', cursor.rowcount, ' записей')

        zap = (dt("2024-01-01 0:0:0"), 0,"Новый год")
        cursor.execute(f"INSERT INTO {pTable} (datetime,type, description) VALUES (?, ?, ?)", zap)
        print('добавили ', cursor.rowcount, ' записей')

        zaps = [(dt("2024-02-23 0:0:0"), 0,"День защитника отечества"),
                 (dt("2024-03-08 0:0:0"), 0,"Международный женский день"),
                 (dt("2024-05-01 0:0:0"), 0,"Праздник Весны и Труда"),
                 (dt("2024-05-09 0:0:0"), 0,"День Победы"),
                 (dt("2024.06.12 0:0:0"), 0,"День России"),
                 ]
        cursor.executemany(f"INSERT INTO {pTable} (datetime,type, description) VALUES (?, ?, ?)", zaps)
        print('добавили ', cursor.rowcount, ' записей')

        dates = [(dt("2024.01.02 0:0:0"), 0,"Новогодние каникулы"),
                 (dt("2024.01.03 0:0:0"), 0,"Новогодние каникулы"),
                 (dt("2024-01-04 0:0:0"), 0,"Новогодние каникулы"),
                 (dt("2024.01.05 0:0:0"), 0,"Новогодние каникулы"),
                 (dt("2024.01.06 0:0:0"), 0,"Новогодние каникулы"),
                 (dt("2024.01.07 0:0:0"), 0,"Новогодние каникулы"),
                 (dt("2024.01.08 0:0:0"), 0,"Новогодние каникулы"),

                 ]
        cursor.executemany(f"INSERT INTO {pTable} (datetime,type, description) VALUES (?, ?, ?)", dates)
        print('добавили ', cursor.rowcount, ' записей')

        zap = (dt(datetime.datetime.now()), 100,"!!TEST!!!!")
        cursor.execute(f"INSERT INTO {pTable} (datetime,type, description) VALUES (?, ?, ?)", zap)
        print('добавили ', cursor.rowcount, ' записей')

        zap = (dt("2024-07-14 0:0:0"), -1, "День взятия Бастилии")
        cursor.execute(f"INSERT INTO {pTable} (datetime,type, description) VALUES (?, ?, ?)", zap)
        print('добавили ', cursor.rowcount, ' xxзаписей')

        zap = (dt("2024-12-28 0:0:0"), 1, "За 2024.12.30")
        cursor.execute(f"INSERT INTO {pTable} (datetime,type, description) VALUES (?, ?, ?)", zap)
        print('добавили ', cursor.rowcount, ' записей')

        connection.commit()

    except Exception as e:
        print('ошибка с БД', e)
    finally:
        cursor.close()
        closeDB(connection)
    print('инициализация закончена')

def getTable(p_connection,pTable):
    if len(pTable) == 0: return False
    try:
        xdata=[]
        xcursor = p_connection.cursor()

        xsql=f"SELECT * FROM {pTable} where type between -9 and 9 order by 2"
        xcursor.execute(xsql)
        xcolumns = [column[0] for column in xcursor.description]
        #print(xcolumns)
        xrows = xcursor.fetchall()

        for row in xrows:
          xdata.append(dict(zip(xcolumns,row)))

        return xdata

    except Exception as e:
        print('ошибка с БД', e)
    finally:
        xcursor.close()
