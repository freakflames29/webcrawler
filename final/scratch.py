import requests as rq
from bs4 import BeautifulSoup as bs

r = rq.get('https://bhairabgangulycollege.ac.in/research-innovation/research-projects-by-faculty-members/')
soup = bs(r.content, 'html.parser')
list = soup.select('#content li')
text=[]
# list = soup.find_all('li',string='Physics')
for i in list:
    # print(i.text)
    text.append(i.text.strip())
    # text.append("+")
    # print()

divison=[]
for i in text:
    tmp=i.replace('“','"')
    qindex=tmp.find('"')
    department=tmp.find('Department')

    divison.append(tmp[:department])
    divison.append(tmp[department:qindex])
    divison.append(tmp[qindex:])

for i in range(len(divison)):
    print(i," ",divison[i])