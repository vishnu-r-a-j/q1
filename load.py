import sqlite3,csv
from tssplit import tssplit
conn = sqlite3.connect("nba.sqlite")
cur = conn.cursor()
with open('nba.csv','r') as file:
    no_record = 0
    for row in file:
        cur.execute("INSERT INTO t1 VALUES(?,?,?,?,?,?,?,?,?,?,?)",tssplit(row,quote='"',delimiter=','))
        conn.commit()
        no_record+=1
conn.close()
print('\n{} Records Transferred'.format(no_record))
