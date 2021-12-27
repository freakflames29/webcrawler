# nit bhopal
import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class NitBhp:
    def __init__(self):
        self.url = 'http://www.manit.ac.in/content/area-research'

    def db_save(self, link):
        mycur = mydb.cursor()
        sql = "INSERT INTO nit_bhop  VALUES (NULL,'%s');" % (link)
        mycur.execute(sql)
        mydb.commit()
        mycur.close()
        print('nit bhopal links saved')
    def scrap(self):
        data = rq.get(self.url)
        soup = bs(data.content, 'html.parser')
        links = soup.select('.even .quick a')
        for link in links:
            # print(link.text)
            self.db_save(link.get('href'))

ob = NitBhp()
ob.scrap()
