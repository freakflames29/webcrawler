import time

from DB_CON import mydb
import requests as rq
from bs4 import BeautifulSoup as bs


class IIT_HYD_GS:
    def __init__(self):
        self.ourl = "https://scholar.google.com"
        mycursor = mydb.cursor()
        sql = "select id,name from iit_hyd;"
        mycursor.execute(sql)
        self.iit_hyd = mycursor.fetchall()
        mycursor.close()

    def gs_scrap(self, name,id):
        space = name.replace(" ", "%20")
        url = "https://scholar.google.com/scholar?q=%s" % space
        page = rq.get(url)
        soup = bs(page.content, 'html.parser')
        names = soup.select('.gs_rt2 a')
        for name in names:
            newurl = self.ourl + name.get('href')
            newrq = rq.get(newurl)
            new_soup = bs(newrq.content, 'html.parser')
            metas = new_soup.find_all('meta')
            for meta in metas:
                if "iit Hyderabad".casefold() in meta.get(
                        'content').casefold() or "Indian Institute of Technology Hyderabad".casefold() in meta.get(
                    'content').casefold():
                    mycur = mydb.cursor()
                    sql = "update iit_hyd set google_scholar='%s' where id='%s'" % (newurl, id)
                    mycur.execute(sql)
                    mydb.commit()
                    # print("updated",name.text)
                    # print(name.text, newurl)
                    break
    def run(self):
        for i in self.iit_hyd:
            self.gs_scrap(i[1],i[0])
            time.sleep(1)

