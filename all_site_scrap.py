from proxy import proxies
from user_agent import user_agents
import requests
from bs4 import BeautifulSoup
Position=[]
Companies=[]
Cities=[]
Stipend=[]
Apply_by=[]
Duration=[]
Hiring_actively=[]
#Scrapping from Linkedin
headers = {"User-Agent":  "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",}
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
