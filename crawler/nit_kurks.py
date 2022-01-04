# nit kurukshetra

import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class NitKuruk:
    def __init__(self):
        self.url = "http://www.nitkkr.ac.in/sub_courses.php?id=24&id3=35"
        self.names = []

    def db_save(self, name):

        mycursor = mydb.cursor()
        sql = "INSERT INTO nit_kuruk VALUES (NULL,'%s',NULL)" % (name)
        mycursor.execute(sql)
        mydb.commit()
        # print(mycursor.rowcount, "record inserted.")

    def scrap(self):
        print("Finding profiles...")
        req = rq.get(self.url)
        soup = bs(req.text, "html.parser")

        try:
            for i in range(1, 11):
                selctor = "#main-content > div > div.col-md-12 > div > div > table > tbody > tr:nth-child(" + str(
                    i) + ") > td:nth-child(3)"

                name = soup.select(selctor)
                self.names.append(name)

            for name in self.names:
                self.db_save(name[0].text.strip())

        except AttributeError:
            print("ERROR")



# ALTER TABLE table AUTO_INCREMENT = 1;
