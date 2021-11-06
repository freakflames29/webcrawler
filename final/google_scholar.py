import requests as rq
from bs4 import BeautifulSoup as bs
import db
import sqlite3

con = sqlite3.connect('./new_db')
cur = con.cursor()

names = []
newnames = []
stripnames = []
google_scholar = []
ourl = "https://scholar.google.com"


# function for getting google_scholar column data from database
def get_gs_data():
    cur.execute("SELECT google_scholar FROM users")
    data = cur.fetchall()
    for i in data:
        if i[0] != None:
            print(i[0])


# function for inserting the data into the database

def insertdata(name, department, description):
    cur.execute(
        'INSERT INTO users VALUES(NULL,"{name}","{department}","{description}",NULL,NULL,NULL)'.format(
            name=name,
            department=department,
            description=description))
    print(
        'INSERT INTO users VALUES(NULL,"{name}","{department}","{description}",NULL,NULL,NULL)'.format(
            name=name,
            department=department,
            description=description))
    con.commit()

# function to update google_scholar url
def update(url, id):
    sql = 'UPDATE users SET google_scholar="{url}" WHERE id={id};'.format(url=url, id=id)
    print(sql)

    a = cur.execute(sql)


# function for getting the data from the database
def getdata():
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    for i in data:
        x = {'id': i[0], 'name': i[1]}
        names.append(x)


getdata()
for i in names:
    name = i['name']
    print(name)
    dot = name.find(".")
    comma = name.find(",")
    pi = name.find("PI")
    namenew = name.replace(name[comma:], "")
    gh = {'id': i['id'], 'name': namenew}
    if dot != -1:
        tmp = namenew.replace(namenew[:dot + 1], "")
        h = {'id': i['id'], 'name': tmp}
        newnames.append(h)
    elif pi != -1:
        tmp = namenew.replace(namenew[:pi + 1], "")
        h = {'id': i['id'], 'name': tmp}
        newnames.append(h)
    else:
        newnames.append(gh)
print("-------------------------------------------------------------------------")
# for loop for newnames
for nn in newnames:
    if nn['name'].find(":") == -1 and nn['name'] != "":
        # print(nn['name'])
        h = {'id': nn['id'], 'name': nn['name'].strip()}
        stripnames.append(h)


# google scholar profile check function
def findscholar(r, m, id):
    hash = {}
    s = bs(r.text, 'html.parser')
    meta = s.find_all('meta')
    for i in meta:
        cont = i.get('content')

        if cont.find("Bhairab Ganguly College"):
            print("*" * 15)
            google_scholar_url = ourl + m.get('href')
            hash = {"name": m.text, "url": google_scholar_url, "id": id}
            google_scholar.append(hash)
            update(google_scholar_url, id)
            break
            # sql = 'UPDATE users SET google_scholar="{url}" WHERE id={id}'.format(url=google_scholar_url, id=id)
            # print(sql)
            # if cur.execute(sql):
            #     print("updated")


def request(url, id):
    print(url)
    response = rq.get(url)
    soup = bs(response.text, 'html.parser')
    # print(soup)
    des = soup.select('.gs_rt2 a')
    # des = soup.select('a')
    print(des)
    for m in des:
        # print(m.get('href'))
        r = rq.get(ourl + m.get('href'))
        if r.status_code == 200:
            # pass
            findscholar(r, m, id)


def names_google_scholar_():
    for i in stripnames:
        url = "https://scholar.google.com/scholar?q={x}".format(x=i['name']).replace(" ", "%20")
        request(url, i['id'])


names_google_scholar_()
# for loop for google_scholar
# for i in google_scholar:
#     print(i)
get_gs_data()
# update(ourl,20)
