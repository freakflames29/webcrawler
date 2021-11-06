import final
import  google_scholar
print("Generating profiles...")
import sqlite3

con = sqlite3.connect('./new_db')
cur = con.cursor()


def showdata():
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    for i in data:
        if i != None:
            print('-'*50)
            print()
            print("Name:- " + i[1])
            print("Research:- " , i[2])
            print("Description " , i[3])
            if i[4] != None:
                print("Google scholar profile:- " , i[4])
            if i[5] != None:
                print("google patent:- " , i[5])
            if i[6] != None:
                print("google patent:- " , i[6])
            print('-'*50)
            print()


showdata()
