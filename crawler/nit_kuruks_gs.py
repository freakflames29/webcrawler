# nit kurukshetra gs
import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class NitKurk:
    def __init__(self):
        self.ourl = "https://scholar.google.com"

        mycursor = mydb.cursor()
        sql = "SELECT id,name FROM nit_kuruk;"
        mycursor.execute(sql)
        self.myresult = mycursor.fetchall()

    def google_scholar(self, name, id):
        # print(name)
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
                if " NIT Kurukshetra".casefold() in meta.get(
                        'content').casefold() or "National Institute of Technology, Kurukshetra".casefold() in meta.get(
                    'content').casefold():
                    mycur = mydb.cursor()
                    sql = "update nit_kuruk set google_scholar='%s' where id='%s'" % (newurl, id)
                    mycur.execute(sql)
                    mydb.commit()
                    print("updated", name.text)
                    # print(name.text, newurl)
                    break

    def start(self):
        for row in self.myresult:
            # self.google_scholar(row[1], row[0])
            if "Dr." in row[1]:
                new_name = row[1].replace("Dr.", "")
                self.google_scholar(new_name, row[0])
            elif "Prof." in row[1]:
                new_name = row[1].replace("Prof.", "")
                self.google_scholar(new_name, row[0])


ob = NitKurk()
ob.start()
