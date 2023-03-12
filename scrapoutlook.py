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
for link in soup.find_all('a',
                          attrs={'href': re.compile("^https://skilloutlook.com/phd-research/")}):
    li.append(link.get('href'))
print(li)
#     print(link)
#     display the actual urls
#     print(link.get('href'))
# ears = soup.find_all('div', class_="entry")
# print(ears)
# for data in soup.find_all("p"):
#     ni.append(data.get_text())
# print(ni[40])
# print(len(ni))