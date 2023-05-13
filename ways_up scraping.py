import requests
from bs4 import BeautifulSoup
import time
time.sleep(1)
proxy={ 'http': 'http://135.181.137.85:3128'}
url = "https://www.wayup.com/s/internships/summer/"
headers={"User-Agent":  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"}
response = requests.get(url, headers=headers,proxies=proxy,timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.text)
companies=[]
cities=[]
role=[]
li=[]

for company in soup.find_all("div",class_="sc-eCApGN cdYXpe"):
    #print(company.text)
    companies.append(company.text)
print(companies)
for city in soup.find_all("div",class_="sc-eCApGN itPUJF"):
    print(city.text)
    cities.append(city.text)
    print(cities)
for position in soup.find_all("h3",class_="sc-bqGHjH fYOHGg"):
    print(position.text)
    role.append(position.text)
    print(role)
for li2 in soup.find_all("span",class_="sc-gKAblj hujHsq"):
    print(li2.text)
    cities.append(li2.text)
    print(li)