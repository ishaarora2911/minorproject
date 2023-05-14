import requests
from bs4 import BeautifulSoup
import time

time.sleep(1)
proxy = {'http':'http://45.61.187.67:4007'}
url = "https://internshala.com/internships/engineering-internship/"
headers = {"User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}
response = requests.get(url, headers=headers, proxies=proxy, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
Type = []
Hiring_actively = []
Position = []
Companies = []
Cities = []
Stipend = []
Apply_by = []
Duration = []
"""
for card in soup.find_all("div", class_="internship_meta"):
  #  working
   actively_hiring_tags = card.find_all("div", class_="actively_hiring_badge")
   if actively_hiring_tags:
       for actively_hiring in actively_hiring_tags:
           span_tags = actively_hiring.find_all("span")
       if span_tags:
           for i in span_tags:
               try:
                   # Extract the desired information from the tag
                   data = i.text.replace("\n", "").strip()
                   Hiring_actively.append(data)
               except AttributeError:
                   # Handle the case when the tag doesn't have the desired information
                   Hiring_actively.append("N/A")
       else:
           # Append "N/A" when the <span> tag is not present
           Hiring_actively.append("N/A")
   else:
       # Append "N/A" when the "actively_hiring_badge" class is not present
       Hiring_actively.append("N/A")


   for header in card.find_all("div", class_="individual_internship_header"):
       for head in header.find_all("div", class_="company"):
            for pos in head.find_all("h3", class_="heading_4_5 profile"):
                for a in pos.find_all("a", class_="view_detail_button"):
                    try:
                        # Extract the desired information from the tag
                        data = a.text.replace("\n", "")
                        data = a.text.strip()
                        Position.append(data)
                    except AttributeError:
                        # Handle the case when the tag is absent or doesn't have the desired information
                        Position.append("N/A")
            for company in head.find_all("h4", class_="heading_6 company_name"):
                data = company.text.replace("\n", "").strip()
                Companies.append(data)

    for details in card.find_all("div",class_="individual_internship_details individual_internship_internship"):
for i in soup.find_all("div",class_="container-fluid individual_internship visibilityTrackerItem"):
        for location in details.find_all("div",id="location_names"):
            for sp in location.find_all("span"):
        for a_tag in i.find_all("a",class_="location_link view_detail_button"):
         data = a_tag.text.replace("\n", "").strip()
         Cities.append(data)








     scraping stipend



    working
    for other_details in card.find_all("div",class_="internship_other_details_container"):
        stipend_tags = card.find_all("div", class_="other_detail_item_row")
        if stipend_tags:
            for i in other_details.find_all("div",class_="other_detail_item_row"):
                for j in i.find_all("div", class_="other_detail_item stipend_container"):


                    for stipend in card.find_all('span',class_='stipend'):
                        data = stipend.text.replace("\n", "").strip()
                        Stipend.append(data)"""
     #scraping duration
"""  
 for period in card.find_all('div',class_="item_body"):
          Duration.append(period.text)
     #scraping start_date
     for startdate in i.find_all('span',class_="start_immediately_desktop"):
          start_date.append(startdate.text)
"""
#print(Hiring_actively)
#print(Position)
#print(Companies)

print(Cities)
# print(Stipend)
#print(Duration)