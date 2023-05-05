import requests
from bs4 import BeautifulSoup
import time
time.sleep(1)
proxy={ 'http': 'http://200.105.215.22:33630'}
url = "https://internshala.com/internships/engineering-internship/"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}
response = requests.get(url, headers=headers,proxies=proxy,timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
li=[]
for i in soup.find_all('div', class_="container-fluid individual_internship visibilityTrackerItem"):
     print(i.text)
     #print(i.type)
     li.append(i.text)

print(li)
