import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class Delhi:
    def __init__(self):
        self.ourl = "https://home.iitd.ac.in"
        self.scrap_url = "https://ird.iitd.ac.in"
        self.names = []
        self.removed_names = []
        self.names_dic = {}
        self.profinfo = []

    def db_insert(self, name, desc):
        mycursor = mydb.cursor()
        sql = "INSERT INTO iit_delhi (id,name,description,google_scholar) VALUES (NULL,'%s','%s',NULL);" % (name, desc)
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    def scrap_info(self):
        r = rq.get(self.scrap_url, verify=False)
        soup = bs(r.content, "html.parser")
        data = soup.select('.content .clearfix table td')
        for x in data:
            self.names.append(x.text.strip())

        start_index = self.names.index('Deptt.of Appl.Mech.')
        end_index = self.names.index('Prof. Aditeshwar Seth')

        for prof in range(start_index, end_index + 1):

            if "Dr. " in self.names[prof]:
                removed = self.names[prof].replace("Dr.", "")
                self.removed_names.append(removed)

            elif "Prof. " in self.names[prof]:
                removed = self.names[prof].replace("Prof.", "")
                self.removed_names.append(removed)

            else:
                self.removed_names.append(self.names[prof])

        print(len(self.removed_names))

        # making the names to dictionary and appending to new list

        for x in range(len(self.removed_names) - 1):
            self.names_dic = {"desc": self.removed_names[x], "name": self.removed_names[x + 1]}
            self.profinfo.append(self.names_dic)

        for prof in self.profinfo:
            # self.db_insert(prof['name'], prof['desc'])
            print(prof['name'])


obj = Delhi()
obj.scrap_info()
