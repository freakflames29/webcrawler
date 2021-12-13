import requests as rq
from bs4 import BeautifulSoup as bs

r = rq.get('https://bhairabgangulycollege.ac.in/research-innovation/research-projects-by-faculty-members/')
soup = bs(r.content, 'html.parser')
list = soup.select('#content li')
text = []
for i in list:
    text.append(i.text)


divison = []
for i in text:
    tmp = i.replace('“', '"')
    qindex = tmp.find('"')
    department = tmp.find('Department')
    hash={"name":tmp[:department].strip(),"department":tmp[department:qindex].strip(),"description":tmp[qindex:].strip()}
    # divison.append(tmp[:department])
    # divison.append(tmp[department:qindex])
    # divison.append(tmp[qindex:])
    divison.append(hash)

for i in range(len(divison)):
    print(i, " ", divison[i]['description'])
    print()
