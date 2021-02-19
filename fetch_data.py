import sqlite3

def readSqliteTable(eid):
    try:
        sqliteConnection = sqlite3.connect('app.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from people where eid = ?"""
        cursor.execute(sqlite_select_query, (eid,))
        records = cursor.fetchall()
        #print("Total rows are:  ", len(records))
        print("Printing EID", eid)
        for row in records:
            print("id: ", row[0])
            print("first_name: ", row[1])
            print("last_name: ", row[2])
            print("eid: ", row[3])
            print("e-mail: ", row[4])
            print("phone: ", row[5])
            print("gen: ", row[6])
            print("cls: ", row[7])
            print("Adr: ", row[8])
            print("bgr: ", row[9])
            print("fname: ", row[10])
            print("mname: ", row[11])
            print("dob: ", row[12])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable(51112)