# nit kurukshetra

import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class NitKuruk:
    def __init__(self):
        self.url = "http://www.nitkkr.ac.in/sub_courses.php?id=24&id3=35"

    def scrap(self):
        req = rq.get(self.url)
        soup = bs(req.text, "html.parser")
        table = soup.select(".table-responsive table")
        i=1
        for name in table:
            prop=name.text.strip()
            if prop!="" and prop!="\n":
                print(i,prop)
                i+=1


ob = NitKuruk()
ob.scrap()
