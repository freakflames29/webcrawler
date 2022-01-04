# nit karnatak
import requests as rq
from bs4 import BeautifulSoup as bs
from DB_CON import mydb


class NitKarnatk:
    def __init__(self):
        self.home_url = "https://www.nitk.ac.in"
        self.starurl = "https://www.nitk.ac.in/research-areas"
        self.deptlinks = []

    def db_save(self, name, profile_link):
        mycur = mydb.cursor()
        sql = "INSERT INTO nit_karnatak VALUES(NULL,'%s','%s',NULL);" % (name, profile_link)
        mycur.execute(sql)
        mydb.commit()
        # print(name," saved")


    def find_profiles(self, link):
        thelink = link.replace("/faculty", "")
        # print(link)
        page = rq.get(link)
        soup = bs(page.content, 'html.parser')
        profiles = soup.select(".item-list .views-row span a")
        for profile in profiles:
            # print(profile.text, " ", thelink + profile.get('href'))
            self.db_save(profile.text, thelink + profile.get('href'))

    def find_dept_links(self):
        page = rq.get(self.starurl)
        soup = bs(page.content, 'html.parser')
        dept_links = soup.select(".gdlr-core-course-item-list a")
        for link in dept_links:
            self.deptlinks.append(link.get('href'))
        for link in self.deptlinks:
            self.find_profiles(link.replace("research-consultancy", "faculty"))


