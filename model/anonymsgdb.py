import sqlite3
from datetime import datetime
from os.path import exists

con = sqlite3.connect("anonymsgdb.db")
cur = con.cursor()

def main():
    try:
        cur.execute('''CREATE TABLE IF NOT EXISTS anonymous (
            id INTEGER PRIMARY KEY ,
            sender_id VARCHAR(25),
            receiver_id VARCHAR(25),
            
            dm VARCHAR(5000),
            reply int,
            date VARCHAR(12),
            
            )''')
      #print("Table created")

    except sqlite3.Error as error:
        print("unable to create database table", error)


    test = cur.execute("SELECT * FROM verifi WHERE ROWID IN ( SELECT max( ROWID ) FROM verifi );")
    test0 = ()
    for i in test:
        test0 = i


    if len(test0) == 0:
        try:
            cur.execute("INSERT INTO verifi VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (
                                                                  "creator0000",
                                                                  "00000000022331",
                                                                
                                                                    "355775675675467753",
                                                                    "546757676768673433",

                                                                   1,
                                                                   "3456789532345678",

                                                                   1,
                                                                   "3456896323456768",

                                                                  "2024-12-12",
                                                                  "2023-10-03"))
            print(">>>   Default Values Inputed")
            con.commit()

        except sqlite3.Error as error:
            print(">>>   Unable To Input Default Data >> ", error)

    else:
        print(">>>   Default Data Already Exist")


if __name__ == '__main__':
  main()