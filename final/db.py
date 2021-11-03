import sqlite3

con = sqlite3.connect('./rdp')
cur = con.cursor()
cur.execute("Insert into rdp values (null,'Hello world','Programming',null,null,null)")
for row in cur.execute('SELECT * FROM rdp'):
    print(row)
