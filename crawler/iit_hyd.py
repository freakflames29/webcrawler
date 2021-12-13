import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class IIT_HYD:
    def __init__(self):
        self.ourl = "https://iith.ac.in"
        self.start_URL = "https://iith.ac.in/research/researchHighlights/"  # Start URL
        self.links = []  # List to store the useful links
        self.name = self.dept = self.desc = ""
        self.info = []  # List to store the data

    def find_links(self, url):
        print("Finding useful links...")
        r = rq.get(url)
        soup = bs(r.content, 'html.parser')
        a = soup.select('.row a')  # Find all the links in row div
        links = []
        for i in a:
            if i.get('href') is not None and i.get('href').startswith('/research/highlights'):  # If the link is useful
                links.append(self.ourl + i.get('href'))  # Append the useful link

        self.links = list(dict.fromkeys(links))  # Remove duplicates

    def insert_db(self, name, desc, project):
        mycursor = mydb.cursor()
        sql = "insert into iit_hyd (id,name,description,google_scholar,project) values(NULL,'%s','%s',NULL,'%s')" % (
            name, desc, project)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    def scrap(self):
        print("Finding researchers...")
        hash = {}
        for url in self.links:
            r = rq.get(url)
            s = bs(r.content, 'html.parser')
            table = s.select('table td')  # Find all the table data
            for i in table:
                if "20%" in i.get("style"):  # Name in the table
                    self.name = i.text.strip()
                elif "30%" in i.get("style"):  # Department in the table
                    self.dept = i.text.strip()
                elif "50%" in i.get("style"):  # Description in the table
                    self.desc = i.text.strip()
                if self.name != "" and self.dept != "" and self.desc != "":  # If all the fields are filled
                    hash = {"name": self.name, "dept": self.dept, "project": self.desc}  # Hash to store the data
                    self.desc = self.name = self.dept = ""  # Reset the fields
                    self.info.append(hash)  # Append the hash to the list
        for i in self.info:
            self.insert_db(i["name"], i["dept"], i["project"])  # Insert the data into the database

    def run(self):
        self.find_links(self.start_URL)  # Find the useful links
        self.scrap()  # Scrap the data


ob = IIT_HYD()
ob.run()
