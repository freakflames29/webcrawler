import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class IIT_BOMB_GS:
    def __init__(self):
        self.ourl = "https://scholar.google.com"

        mycursor = mydb.cursor()
        sql = "SELECT id,name FROM iit_bomb"
        mycursor.execute(sql)
        self.myresult = mycursor.fetchall()
        # for i in range(len(myresult)):
        #   name = myresult[i][1]
        #   id = myresult[i][0]
        #   if name.startswith('PI:'):
        #       print(name, id)

    def google_scholar(self, name, id):
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
                if "iit Bombay".casefold() in meta.get(
                        'content').casefold() or "Indian Institute of Technology Bombay".casefold() in meta.get(
                    'content').casefold():
                    mycur = mydb.cursor()
                    sql = "update iit_bomb set google_scholar='%s' where id='%s'" % (newurl, id)
                    mycur.execute(sql)
                    mydb.commit()
                    print("updated", name.text)
                    # print(name.text, newurl)
                    break

    def run(self):
        for i in self.myresult:
            name = i[1]
            id = i[0]
            clean_name = name.replace("PI: Prof.", "")
            self.google_scholar(clean_name, id)


ob = IIT_BOMB_GS()
ob.run()
