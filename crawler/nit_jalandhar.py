#nit jalandhar
import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb

class NitJala:
    def __init__(self):
        self.url="https://www.nitj.ac.in/index.php/nitj_cinfo/index/71"
    def db_save(self,info):
        mycur=mydb.cursor()
        sql="insert into nit_jal  values(NULL,'%s');"%(info)
        mycur.execute(sql)
        mydb.commit()
        print("saved")

    def scrap(self):
        req=rq.get(self.url)
        soup=bs(req.content,"html.parser")
        names=soup.select(".row ol li")
        for name in names:
            name=name.text.strip()
            self.db_save(name)

ob=NitJala()
ob.scrap()
