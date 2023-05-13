import requests
from bs4 import BeautifulSoup
import time
time.sleep(1)
proxy={ 'http': 'http://135.181.137.85:3128'}
url = "https://internship.aicte-india.org/./fetch_city.php?city=Nicobar"
headers={"User-Agent":  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"}
response = requests.get(url, headers=headers,proxies=proxy,timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.text)
headings=[]
# for card in soup.find_all("div", class_="internship-info"):
#
#     for heading in card.find_all("div", class_="internship-primary-info"):
#
#         for k in heading.find_all("div"):
#             for j in k.find_all("h3", class_="job-title"):
#                 # print(heading.text)
#                 headings.append(j.text)
# print(headings)
companies=[]
for card in soup.find_all("div", class_="internship-info"):

    for heading in card.find_all("div", class_="internship-primary-info"):

        for k in heading.find_all("div"):
            for company in k.find_all("h5", class_="company-name"):
                companies.append(company)
print(companies)