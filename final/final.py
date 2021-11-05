import requests as rq
from bs4 import BeautifulSoup as bs


def scrap_url(research_urls):
    #scrapping each url
    for link in research_urls:
        print(link)
        reqs = rq.get(link)
        soup = bs(reqs.text, 'html.parser')
        names = soup.select('#content li ')
        text = []
        # if names != None:
        for z in names:
            text.append(z.text)
        divison = []
        # getting the name,department and description of researcher and storing inside an array
        for i in text:
            tmp = i.replace('“', '"')
            qindex = tmp.find('"')
            department = tmp.find('Department')
            hash = {"name": tmp[:department].strip(), "department": tmp[department:qindex].strip(),
                    "description": tmp[qindex:].strip()}

            divison.append(hash)

        for i in range(len(divison)):
            if divison[i]['department'] != "":
                print(i, " ", divison[i])
                print()


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
