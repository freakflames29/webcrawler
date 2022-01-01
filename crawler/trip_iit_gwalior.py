# IIIT gwalior
import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class IITGwa:
    def __init__(self):
        self.url = "http://www.iiitm.ac.in/index.php/en/research-scholars"
        self.names = []

    def db_save(self, name):
        mycursor = mydb.cursor()
        sql = "insert into trip_gwalior values(NULL,'%s',NULL)" % (name)
        mycursor.execute(sql)
        mydb.commit()
        print(name + "Data inserted")

    def scrapdata(self):
        page = rq.get(self.url)
        soup = bs(page.content, 'html.parser')
        for i in range(2, 50):
            select = "#sppb-addon-1528681171600 > div > div > table > tbody > tr:nth-child({index}) > td:nth-child(2) > p".format(
                index=i)
            # print(select)
            name = soup.select(select)
            self.names.append(name)

    def start(self):
        for j in self.names:
            self.db_save(j[0].text)


ob = IITGwa()
ob.start()  # start method
