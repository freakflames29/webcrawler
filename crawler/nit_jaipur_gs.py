import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class Nit_jaipur_gs:
    def __init__(self):
        self.ourl = "https://scholar.google.com"

        mycursor = mydb.cursor()
        sql = "SELECT id,name FROM nit_jaipur"
        mycursor.execute(sql)
        self.myresult = mycursor.fetchall()

    def google_sch(self,name,id):
        space = name.replace(" ", "%20")
        url = "https://scholar.google.com/scholar?q=%s" % space
        page = rq.get(url)
        soup = bs(page.content, 'html.parser')
        names = soup.select('.gs_rt2 a')
        for name in names:
            newurl = self.ourl + name.get('href')
            newrq = rq.get(newurl)
            new_soup = bs(newrq.content, 'html.parser')
            metas = new_soup.find_all('meta')
            for meta in metas:
                if "MNIT, Jaipur".casefold() in meta.get(
                        'content').casefold() or "Malaviya National Institute of Technology Jaipur".casefold() in meta.get(
                    'content').casefold() or "MNIT Jaipur".casefold() in meta.get(
                        'content').casefold():

                    mycur = mydb.cursor()
                    sql = "update nit_jaipur set google_scholar='%s' where id='%s'" % (newurl, id)
                    mycur.execute(sql)
                    mydb.commit()
                    # print("updated", name.text)
                    # print(name.text, newurl)
                    break

    def start(self):
        for name in self.myresult:
            if name[1].startswith("Prof."):
                new_name = name[1].replace("Prof.", "")

                # print(name)
                self.google_sch(new_name,name[0])
            elif name[1].startswith("Dr."):
                new_name = name[1].replace("Dr.", "")
                # print(name)
                self.google_sch(new_name,name[0])
            elif name[1].startswith("Sh."):
                new_name = name[1].replace("Sh.", "")
                # print(name)
                self.google_sch(new_name,name[0])

ob=Nit_jaipur_gs()
ob.start()
