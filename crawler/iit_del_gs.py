import time

from DB_CON import mydb
import requests as rq
from bs4 import BeautifulSoup as bs


class IIT_DEL_GS:
    def __init__(self):
        self.ourl = "https://scholar.google.com"
        mycursor = mydb.cursor()
        sql = "select id,name from iit_delhi;"
        mycursor.execute(sql)
        self.names = mycursor.fetchall()

    def scrap(self, name, id):
        print("Finding other profiles...")
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
                if "iit Delhi".casefold() in meta.get(
                        'content').casefold() or "Indian Institute of Technology Delhi".casefold() in meta.get(
                        'content').casefold():
                    mycur = mydb.cursor()
                    sql = "update iit_delhi set google_scholar='%s' where id='%s'" % (newurl, id)
                    mycur.execute(sql)
                    mydb.commit()
                    break

    def run(self):
        print("Finding profiles...")
        for i in self.names:
            self.scrap(i[1], i[0])
            time.sleep(1)


# gs = IIT_DEL_GS()
# gs.run()