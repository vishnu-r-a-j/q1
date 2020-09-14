import sqlite3
conn = sqlite3.connect("nba.sqlite")
cur = conn.cursor()

sql = """
      CREATE TABLE t1(
         A INTEGER,
         B DATE,
         C TEXT,
         D TEXT,
         E INTEGER,
         F TEXT,
         G INTEGER,
         H TEXT,
         I TEXT,
         J INTEGER,
         K TEXT

         )"""

cur.execute(sql)
print("Table has been created")
conn.commit()
conn.close()
