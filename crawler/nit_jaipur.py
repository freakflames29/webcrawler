# nit jaipur
import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class NitJaipur:
    def __init__(self):
        self.url = "http://mnit.ac.in/research/preprofile.php"

    def db_save(self, info):
        mycur = mydb.cursor()
        sql = "insert into nit_jaipur  values(NULL,'%s',NULL);" % (info)
        mycur.execute(sql)
        mydb.commit()
        # print("saved")

    def scrap(self):
        print("Finding profiles...")
        req = rq.get(self.url)
        soup = bs(req.text, "html.parser")
        names = soup.select('.TabbedPanelsContent td b')
        for name in names:
            self.db_save(name.text.strip())


