import requests as rq
from bs4 import BeautifulSoup as bs


def scrap_url(research_urls):
    for link in research_urls:
        reqs = rq.get(link)
        soup = bs(reqs.text, 'html.parser')
        names = soup.select('#content li strong')
        if names != None:
            for name in names:
                print(name.text)


def callurls(urlname):
    orUrl = 'https://bhairabgangulycollege.ac.in/'
    # print("urlname:" + urlname)
    reqs = rq.get(urlname)
    soup = bs(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    # print(len(urls))
    for i in urls:
        # print(i)
        if i == "https://bhairabgangulycollege.ac.in/" or i == "/":
            continue
        elif (urls.count(i) == 0):
            callurls(orUrl + i)

    newurls = list(set(urls))
    research_urls = []
    for i in newurls:
        if i is not None and i.find("research") != -1:
            if i.find(urlname) == -1:

                research_urls.append(urlname + i)
            else:
                research_urls.append(i)

    scrap_url(research_urls)


try:
    url = "https://bhairabgangulycollege.ac.in/"
    callurls(url)

except Exception as e:
    print(e)
