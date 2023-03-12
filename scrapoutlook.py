import re

import requests
from bs4 import BeautifulSoup
url = "https://skilloutlook.com/career-corner/four-iits-announce-summer-research-internship-programs-2023-for-university-students"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.49"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
#print(response.text)
# print(soup.title)
li=[]
ni=[]
for i in soup.find_all('div',id='entryContainer'):
    for link in i.find_all('a',
                          attrs={'href': re.compile("^https://skilloutlook.com/")}):
        li.append(link.get('href'))
print(li)
for j in range(0,1):
    i=li[j]
    print("link=",i)
    url2=i
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.49"}
    response2 = requests.get(url2, headers=headers)
    soups = BeautifulSoup(response2.text, "html.parser")
    for j in soups.find_all('div',id='entryContainer'):
        # for data in j.find_all('div',id='entryContainer'):
        for j2 in j.find_all('p'):
        #     pattern = re.compile("https://",j2)
        #     if pattern:
        #         pass
        #     else:
                print("1:",j2.text)

    #print(response2.text)

#     print(link)
#     display the actual urls
#     print(link.get('href'))
# ears = soup.find_all('div', class_="entry")
# print(ears)
# for data in soup.find_all("p"):
#     ni.append(data.get_text())
# print(ni[40])
# print(len(ni))