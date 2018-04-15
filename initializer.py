import pandas as pd
import sqlite3

db = sqlite3.connect('books.db')
dfs = pd.read_excel('books.xlsx', sheet_name=None)
for table, df in dfs.items():
    df.to_sql(table, db,index=False,if_exists="replace")
cursor = db.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
a=cursor.fetchall()
if a[0][0]!='data':
    cursor.execute("ALTER TABLE '%s' RENAME TO data"%a[0][0])
cursor.execute("ALTER TABLE data ADD COLUMN books_left INTEGER")
cursor.execute("ALTER TABLE data ADD COLUMN reserved_books INTEGER")
cursor.execute("ALTER TABLE data ADD COLUMN takenList TEXT")
cursor.execute("ALTER TABLE data ADD COLUMN reserved_list TEXT")
cursor.execute("SELECT book_count FROM data")
a=cursor.fetchall()
for i in a:
    cursor.execute("UPDATE data SET books_left=(?) WHERE books_left is NULL LIMIT 1",(i))
    cursor.execute("UPDATE data SET reserved_books=(?) WHERE reserved_books is NULL LIMIT 1",(0,))
cursor.execute("SELECT * FROM data")
for rows in cursor.fetchall():
    print rows
db.commit()
cursor.close()
db.close()
