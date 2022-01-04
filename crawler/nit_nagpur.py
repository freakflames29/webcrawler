#nit nagpur
import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class NitNag:
    def __init__(self):
        self.url = "https://vnit.ac.in/index.php/rdprojects/"

    def dbsave(self, name):
        mycursor = mydb.cursor()
        sql = "INSERT INTO nit_nagpur  VALUES (NULL,'%s',NULL)" % (name)
        mycursor.execute(sql)
        mydb.commit()

    def scrap(self):
        print("Finding profiles...")
        req = rq.get(self.url)
        soup = bs(req.content, 'html.parser')
        names = soup.select('.fruitful_tab tbody td')
        for name in names:
            if name.get('style') == 'width: 22.4628%; padding-left: 15px;':
                self.dbsave(name.text.strip())


