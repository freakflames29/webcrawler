# nit nagpur gs
import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class NitNagGs:
    def __init__(self):
        self.ourl = "https://scholar.google.com"

        mycursor = mydb.cursor()
        sql = "SELECT id,name FROM nit_nagpur;"
        mycursor.execute(sql)
        self.myresult = mycursor.fetchall()

    def google_scholar(self, name, id):
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
                if "VNIT, nagpur".casefold() in meta.get(
                        'content').casefold() or "Visvesvaraya National Institute of Technology, Nagpur".casefold() in meta.get(
                    'content').casefold() or "VNIT nagpur".casefold() in meta.get(
                        'content').casefold():
                    mycur = mydb.cursor()
                    sql = "update nit_nagpur set google_scholar='%s' where id='%s'" % (newurl, id)
                    mycur.execute(sql)
                    mydb.commit()
                    print("updated", name.text)
                    # print(name.text, newurl)
                    break
    def start(self):
        for i in self.myresult:
            if "Dr." in i[1]:
                new_name=i[1].replace("Dr.","")
                self.google_scholar(new_name, i[0])


ob=NitNagGs()
ob.start()