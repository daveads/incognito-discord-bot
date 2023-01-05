import sqlite3
from datetime import datetime


datenow = datetime.now()

datenow.strftime("%d/%m/%Y %H:%M")

con = sqlite3.connect("confess.db")
cur = con.cursor()

from os.path import exists
file_exists = exists('confess.db')

try:

    cur.execute('''CREATE TABLE confession (
            date VARCHAR(255),
            author VARCHAR(255),
            author_id int,
            confession VARCHAR(3000),
            count int
            )''')
except:
  pass


test = cur.execute("SELECT * FROM confession WHERE ROWID IN ( SELECT max( ROWID ) FROM confession );")
test0 = ()
for i in test:
    test0 = i

if len(test0) == 0:
    cur.execute("INSERT INTO confession VALUES (?, ?, ?, ?, ?)", ("default", 
                                                                  "default", 
                                                                  0, 
                                                                  "default",
                                                                  0))
    print("default values inputed")
    con.commit()

class confess_data():

    def __init__(self, date, author, author_id, confession, count):

        self.date = date
        self.author = author
        self.author_id = author_id
        self.confession = confession
        self.count = count

        cur.execute("INSERT INTO confession VALUES (?, ?, ?, ?, ?)", (self.date, self.author, self.author_id, self.confession, self.count))

        con.commit()



#data format
"""
Date #done
***
confession   #done
***
confession_count ? //maybe
***
author_name #done
author_id #done
"""
