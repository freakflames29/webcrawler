import sys
import time
#importing mydb from the DB folder
#sys.path.insert(0, '/home/sourav/Documents/webcrawler/code/DB')
from DB_CON import mydb
import requests as rq
from bs4 import BeautifulSoup as bs

ourl = "https://scholar.google.com"

#function for finding correct profile and updating the db profile link
def google_scrap(name,id):
    url = "https://scholar.google.com/scholar?q=%s"%name
    page = rq.get(url)
    soup = bs(page.content, 'html.parser')
    names = soup.select('.gs_rt2 a')
    for name in names:
        newurl = ourl + name.get('href')
        newrq = rq.get(newurl)
        new_soup = bs(newrq.content, 'html.parser')
        metas = new_soup.find_all('meta')
        for meta in metas:
            if "iit kanpur" in meta.get('content').casefold() or "Indian Institute of Technology Kanpur".casefold() in meta.get('content').casefold():
               mycur = mydb.cursor()
               sql="update iit_kan set google_scholar='%s' where id='%s'"%(newurl,id)
               mycur.execute(sql)
               mydb.commit()
               # print("updated")
               break


try:
    print("Finding profiles...")
    #selecting all names amd ids from the db
    mycursor=mydb.cursor()
    sql="select id,name from iit_kan;"
    mycursor.execute(sql)
    myresult=mycursor.fetchall()
    for row in myresult:
        name=row[1] #tuple row 1 is name and row 0 is id
        removed_space=name.replace(" ","%20")
        google_scrap(removed_space,row[0])
        time.sleep(1)
except Exception as e:
    print(e)
