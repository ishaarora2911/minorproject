import requests
from bs4 import BeautifulSoup
import time
time.sleep(1)
proxy={ 'http': 'http://51.79.50.31:9300'}
url = "https://internshala.com/internships/engineering-internship/"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"}
response = requests.get(url, headers=headers,proxies=proxy,timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
li=[]
headings=[]
companies=[]
stipends=[]
city=[]
duration=[]
start_date=[]

for i in soup.find_all('div', class_="container-fluid individual_internship visibilityTrackerItem"):
     print(i.text)
     print(i.type)

     li.append(i.text)
     #scraping headings
     for heading in i.find_all('h3',class_="heading_4_5 profile"):
          #print(heading.text)
          headings.append(heading.text)


     #scraping companiess
     for company in i.find_all('a',{"class":"link_display_like_text view_detail_button"}):
             #  print(company.text)
          companies.append(company.text)
     #scraping stipend
     for stipend in i.find_all('span',class_='stipend'):
          stipends.append(stipend.text)
     #scraping duration
     for period in i.find_all('div',class_="item_body"):
          duration.append(period.text)
     #scraping start_date
     for startdate in i.find_all('span',class_="start_immediately_desktop"):
          start_date.append(startdate.text)
     #Scraping cities
     for cities in i.find_all('a' ,{"class": "location_link view_detail_button"}):
          print(cities.text)
          city.append(cities.text)


print(companies)
print(stipends)
print(duration)
print(start_date)
print(city)
print(headings)