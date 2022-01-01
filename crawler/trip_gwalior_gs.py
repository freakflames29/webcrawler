# trip gwalior gs
import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb

class TripGwaGs:
    def __init__(self):
        self.ourl = "https://scholar.google.com"

        mycursor = mydb.cursor()
        sql = "SELECT id,name FROM trip_gwalior;"
        mycursor.execute(sql)
        self.myresult = mycursor.fetchall()

    def google_scholar(self, name, id):
        print(name)
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
                if "ABV-IIITM Gwalior".casefold() in meta.get('content').casefold() or "Atal Bihari Vajpayee Indian Institute of Information Technology and Management, Gwalior".casefold() in meta.get('content').casefold():
                    mycur = mydb.cursor()
                    sql = "update trip_gwalior set google_scholar='%s' where id='%s'" % (newurl, id)
                    mycur.execute(sql)
                    mydb.commit()
                    print("updated", name.text)
                    # print(name.text, newurl)
                    break
    def start(self):
        for row in self.myresult:
            self.google_scholar(row[1], row[0])
ob=TripGwaGs()
ob.start()

#
# "NITK, karanatak".casefold() in meta.get(
#                         'content').casefold() or "karanatak National Institute of Technology, karanatak".casefold() in meta.get(
#                     'content').casefold() or "NITK karanatak".casefold() in meta.get(
#                         'content').casefold() or