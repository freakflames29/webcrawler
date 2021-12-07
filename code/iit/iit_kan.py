import time

import requests as rq
from bs4 import BeautifulSoup as bs
import mysql.connector

#the main url
user_url = "https://www.iitk.ac.in"



# database connection

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="webcrawler"
)


# inserting names into database
def insert_names(data):
    mycursor = mydb.cursor()
    sql = "INSERT INTO iit_kan (id,name,description,google_scholar) VALUES (NULL, '%s',NULL,NULL);" % (data)
    mycursor.execute(sql)
    mydb.commit()

# to store description accotding to name
ids = []
last_id = 0 #db first id
fid = 0 # db last id

#fetching all ddatabase ids
def fetch_ids():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id FROM iit_kan")
    datas = mycursor.fetchall()
    mydb.commit()
    for i in datas:
        ids.append(i[0])
    global  last_id
    last_id = ids[len(ids) - 1] # setting last id
    global  fid
    fid = ids[0] #setting first id
    # print(ids)
    # print("First data:", fid, "Second Data:", last_id)


# inserting description into database
def insert_description(data):
    global  fid, last_id
    # print("FID",fid)
    # print("THE LAST ID",last_id)
    if fid <= last_id:
        mycursor = mydb.cursor()
        sql = 'UPDATE iit_kan set description="%s" where id="%s"' % (data, fid)
        mycursor.execute(sql)
        mydb.commit()
        # print(sql)
        fid += 1
        # print(id)




# function to scrap the urls for researcher profiles
def scrap(urllist):
    # for link in urllist:
    res = rq.get(urllist)
    soup = bs(res.text, 'html.parser')
    names = soup.select('.jwts_content td p a')
    profiles = soup.select('.jwts_content table td p')

    print(len(profiles))

    print(len(names))
    z = 1
    x = 1
    descriptions = []
    for name in names:
        if len(name.text) > 0:
            print(z, name.text)
            insert_names(name.text)
        z += 1
    fetch_ids()
    for i in profiles:
        res_loc = i.text.strip().find("Research Topic")

        research_topic = i.text[res_loc:400]

        cleaned_research_topic = research_topic.replace('"', "'")
        if (len(cleaned_research_topic)) != 1:
            print(x, cleaned_research_topic)
            # descriptions.append(cleaned_research_topic)
            insert_description(cleaned_research_topic)
        x += 1


# function for getting all research areas links
def callurls(urlname):
    orUrl = user_url
    # print("urlname:" + urlname)
    reqs = rq.get(urlname)
    soup = bs(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    # print(len(urls))
    for i in urls:
        # print(i)
        if i == "{ul}/".format(ul=user_url) or i == "/":
            continue
        elif urls.count(i) == 0:
            callurls(orUrl + i)

    newurls = list(set(urls))
    research_urls = []
    for i in newurls:
        if i is not None and i.find("research") != -1:
            if i.find(urlname) == -1:

                research_urls.append(urlname + i)
            else:
                research_urls.append(i)

    for i in research_urls:
        print(i)


try:
    scrap("https://www.iitk.ac.in/new/iitk-research-scholars")
except Exception as e:
    print("ERROR", e)
