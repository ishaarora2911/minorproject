import requests
from bs4 import BeautifulSoup
import time
time.sleep(1)
proxy={'http':'http://51.79.50.31:9300'}
#url="https://in.indeed.com/m/jobs?q=B+Tech+Internship&vjk=8f51acd1f3df1dbe"
url="https://in.linkedin.com/jobs/internship-jobs?position=1&pageNum=0"
headers={'User-Agent':"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 13_0_0; en-US; Valve Steam GameOverlay/1676336721; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
response=requests.get(url , headers=headers,proxies=proxy,timeout=10)
soup=BeautifulSoup(response.text,"html.parser")
#print(soup.text)
heading=[]
cities=[]
hiring_timing=[]
companies=[]
# for head in soup.find_all("span",class_="sr-only"):
#     #print(head.text)
#     heading.append(head.text)
# for city in soup.find_all("span",class_="job-search-card__location"):
#     cities.append(city.text)
# for time in soup.find_all("span",class_="result-benefits__text"):
#     hiring_timing.append(time.text)
#for i in soup.find_all("h4",class_="base-search-card__subtitle"):
for company in soup.find_all("a",class_="hidden-nested-link"):
    companies.append(company.text)
# print(heading)
# print(cities)
# print(hiring_timing)
print(companies)