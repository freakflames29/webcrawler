import requests as rq
from bs4 import BeautifulSoup as bs


# from DB_CON import mydb
class IIT_BOMB:
    def __init__(self):
        self.dept_url = ["https://www.che.iitb.ac.in", "https://www.bio.iitb.ac.in"]
        self.start_url = ["https://www.che.iitb.ac.in/research-areas",
                          "https://www.bio.iitb.ac.in/research/research-groups"]


    def find_profile(self, link, count):
        req = rq.get(link)
        soup = bs(req.content, 'html.parser')
        names = soup.select(".view-content .views-field-title span a")
        if names is not None:
            for name in names:
                prof_name = name.text
                desc_link = self.dept_url[count] + name.get('href')
                mycursor = mydb.cursor()
                sql = "INSERT INTO iit_bomb (id,name,description,google_scholar) VALUES (NULL,'%s','%s',NULL)" % (
                    prof_name, desc_link)
                mycursor.execute(sql)
                mydb.commit()
                print(prof_name + "Inserted")


    def new_Scrap(self, link):
        new_rq = rq.get(link)
        new_soup = bs(new_rq.content, 'html.parser')
        names = new_soup.select(
            "#post-2020 > div > div > div > div > section.elementor-section.elementor-top-section.elementor-element.elementor-element-19b0cd25.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default > div.elementor-container.elementor-column-gap-default > div > div .elementor-toggle-item p")
        if names is not None:
            for i in names:
                text = i.text
                pi_loc = text.find('PI:')
                name = text[pi_loc:]
                desc = text[:pi_loc]
                mycursor = mydb.cursor()
                sql = "INSERT INTO iit_bomb (id,name,description,google_scholar) VALUES (NULL,'%s','%s',NULL)" % (
                    name, desc)
                mycursor.execute(sql)
                mydb.commit()
                print(name + "Inserted")


    def scrap(self):
        for url in range(len(self.start_url)):
            page = rq.get(self.start_url[url])
            soup = bs(page.content, 'html.parser')
            links = soup.find_all('a')
            res_links = []
            for link in links:
                if link.get('href') is not None:
                    if link.get('href').startswith('/research-area'):
                        res_url = self.dept_url[url] + link.get('href')
                        if res_url not in res_links:
                            res_links.append(res_url)
            for res_link in res_links:
                print(res_link)
                self.find_profile(res_link, url)
            self.new_Scrap(self.start_url[1])


ob = IIT_BOMB()
ob.scrap()
