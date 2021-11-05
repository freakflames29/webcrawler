import requests as rq
from bs4 import BeautifulSoup as bs
import db
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


def scrap_url(research_urls):
    # scrapping each url
    for link in research_urls:
        print(link)
        reqs = rq.get(link)
        soup = bs(reqs.text, 'html.parser')
        names = soup.select('#content li ')
        text = []
        # if names != None:
        for z in names:
            text.append(z.text)
        divison = []
        # getting the name,department and description of researcher and storing inside an array
        for i in text:
            tmp1 = i.replace('“', '')
            tmp = tmp1.replace('”', '')
            department = tmp.find('Department')
            qindex = tmp.find('.', department + 1)
            name = tmp[:department].strip()
            newdepaartment = tmp[department:qindex].strip()
            description = tmp[qindex + 1:].strip().replace('\n', '. ')

            hash = {"name": name, "department": newdepaartment,
                    "description": description}

            divison.append(hash)

    for i in range(len(divison)):
        if divison[i]['department'] != "":
            zinsertdata(divison[i]['name'], divison[i]['department'], divison[i]['description'])
            # print(divison[i]['name'], divison[i]['department'], divison[i]['description'])
            # print(divison[i])
            # print("name: " + divison[i]['name'])
            # print("department: " + divison[i]['department'])
            # print("description: " + divison[i]['description'])
            # print("\n")


def callurls(urlname):
    orUrl = 'https://bhairabgangulycollege.ac.in/'
    # print("urlname:" + urlname)
    reqs = rq.get(urlname)
    soup = bs(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    # print(len(urls))
    for i in urls:
        # print(i)
        if i == "https://bhairabgangulycollege.ac.in/" or i == "/":
            continue
        elif (urls.count(i) == 0):
            callurls(orUrl + i)

    newurls = list(set(urls))
    research_urls = []
    for i in newurls:
        if i is not None and i.find("research") != -1:
            if i.find(urlname) == -1:

                research_urls.append(urlname + i)
            else:
                research_urls.append(i)

    scrap_url(research_urls)


try:
    url = "https://bhairabgangulycollege.ac.in/"
    callurls(url)
    # db.showdata()
except Exception as e:
    print(e)
