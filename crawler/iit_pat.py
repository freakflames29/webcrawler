import requests as rq
from bs4 import BeautifulSoup as bs

from DB_CON import mydb


def db_insert(name, dept, desc):
    # Insert data into the database
    print("[+] Inserting data into the database...")
    mycursor = mydb.cursor()
    sql = 'INSERT INTO iit_pat (id, name, department, description, google_scholar) VALUES (NULL, "%s", "%s", "%s", NULL);' % (
        name, dept, desc)
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    print("[+] Data inserted successfully!")
    print(mycursor.rowcount, "record inserted.")


class IIT_PAT:
    def __init__(self):
        self.ourl = 'http://www.iitp.ac.in/'
        self.startUrl = 'https://www.iitp.ac.in/index.php/en-us/research/patent-ipr'  # start url
        self.links = []  # List to store important links
        self.name = self.dept = self.desc = ""
        self.info = []
        self.prof_names = []

    def get_links(self):
        # Get all the links from the start url
        print("[+] Getting links from the start url...")
        r = rq.get(self.startUrl)
        soup = bs(r.content, 'html.parser')
        # print(soup.find_all('a'))
        a = soup.select(".inner-right-pannel .item-page .responsive-table table tbody tr td")
        print("[+] Data found!")
        # table = {}
        # print(a[0].text)
        for i in range(0, len(a), 3):
            self.dept = a[i].text
            self.desc = a[i + 1].text
            self.name = a[i + 2].text
            # adding data into the database
            db_insert(self.name, self.dept, self.desc)

            self.prof_names.append(self.name)
            if self.name and self.dept and self.desc is not None:
                table = {'name': self.name, 'dept': self.dept, 'desc': self.desc}
                # print(table)
                self.info.append(table)

        for i in self.prof_names:
            print(i)


ob = IIT_PAT()
ob.get_links()
