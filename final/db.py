import sqlite3

con = sqlite3.connect('./rdp')
cur = con.cursor()


# print(cur)

def insertdata(name, department, description):
    cur.execute(
        'INSERT INTO rdp VALUES(NULL,"{name}","{department}","{description}",NULL,NULL)'.format(
            name=name,
            department=department,
            description=description))
    print(
        'INSERT INTO rdp VALUES(NULL,"{name}","{department}","{description}",NULL,NULL)'.format(
            name=name,
            department=department,
            description=description))
    con.commit()


def showdata():
    cur.execute("SELECT * FROM rdp")
    data = cur.fetchall()
    for i in data:
        print(i)


# insertdata("Hello", "dolly", "lara")
