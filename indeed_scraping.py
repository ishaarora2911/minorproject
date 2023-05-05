import requests
from bs4 import BeautifulSoup
import time
time.sleep(2)
url="https://in.indeed.com/Internship-jobs?vjk=56d0f932faaf9c4b"
proxy={ 'http': 'http://135.181.137.85:3128'}
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
response = requests.get(url, headers=headers,proxies=proxy,timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.text)
li=[]
for i in soup.find_all('div', class_="jobsearch-SerpMainContent"):
    print(i.text)
    li.append(i.text)
print(li)
