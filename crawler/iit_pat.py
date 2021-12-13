import requests as rq
from bs4 import BeautifulSoup as bs


class IIT_PAT:
    def __init__(self):
        self.ourl = 'http://www.iitp.ac.in/'
        self.startUrl = 'https://www.iitp.ac.in/index.php/en-us/research/patent-ipr'  # start url
        self.links = []  # List to store important links
        self.name = self.dept = self.desc = ""
        self.info = []

    def get_links(self):
        # Get all the links from the start url
        print("[+] Getting links from the start url...")
        r = rq.get(self.startUrl)
        soup = bs(r.content, 'html.parser')
        print("[+] Links found!")
        # print(soup.find_all('a'))
        a = soup.select(".inner-right-pannel .item-page .responsive-table table tbody tr td")
        hash = {}
        for i in a:
            print(i.get("style"))
            self.dept = i.text.strip()
            hash = {'dept': self.dept}
            self.info.append(hash)  # for i in self.info:


ob = IIT_PAT()
ob.get_links()
