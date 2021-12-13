import requests as rq
from bs4 import BeautifulSoup as bs


# from DB_CON import mydb
class IIT_BOMB:
    def __init__(self):
        self.ourl = "https://www.iitb.ac.in"
        self.starturl = "https://www.iitb.ac.in/en/education/academic-divisions"
        self.dept_urls = []

    def scrap_departments_url(self):
        page = rq.get(self.starturl)
        soup = bs(page.content, 'html.parser')
        dept_links = soup.select("#node-407 > div.content > div > div > div > div:nth-child(2) a")
        for i in dept_links:
            self.dept_urls.append(i.get('href'))

    def callurls(self, urlname, nochange):
        print("THE URL:", urlname)
        print("Finding urls...")
        orUrl = nochange
        sec_orUrl = nochange.replace("http", "https")
        reqs = rq.get(urlname)
        soup = bs(reqs.text, 'html.parser')
        urls = []
        for link in soup.find_all('a'):
            urls.append(link.get('href'))

        for i in urls:
            # print(i)
            if i == "{ul}/".format(ul=nochange) or i == "/":
                continue
            elif urls.count(i) == 0 and (i.startswith("http") or i.startswith("https")):
                self.callurls(i, nochange)

            elif urls.count(i) == 0:
                self.callurls(orUrl + i, nochange)

        newurls = list(set(urls))
        research_urls = []
        for i in newurls:
            if i is not None and i.find("research") != -1:
                if i.find(urlname) == -1:

                    research_urls.append(urlname + i)
                else:
                    research_urls.append(i)

        for i in research_urls:
            print(i)

    def run(self):
        for i in self.dept_urls:
            url = i[:-1]
            self.callurls(url, url)


ob = IIT_BOMB()
ob.scrap_departments_url()
# ob.callurls("https://www.bio.iitb.ac.in")
ob.run()
