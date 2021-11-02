import requests as rq
from bs4 import BeautifulSoup as bs


def callurls(urlname):
    orUrl = 'https://bhairabgangulycollege.ac.in/'
    # print("urlname:" + urlname)
    reqs = rq.get(urlname)
    soup = bs(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    print(len(urls))
    for i in urls:
        # print(i)
        if i == "https://bhairabgangulycollege.ac.in/" or i == "/":
            continue
        elif (urls.count(i) == 0):
            callurls(orUrl + i)

    newurls = list(set(urls))

    for i in newurls:
        if (i is not None and i.find("research") != -1):
            if (i.find(urlname) == -1):
                print(urlname + i)
            else:
                print(i)


try:
    url = "https://bhairabgangulycollege.ac.in/"
    callurls(url)

except Exception as e:
    print(e)

