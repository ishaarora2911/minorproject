import requests
from bs4 import BeautifulSoup
#Define the URLs of the page to scrape

urls=['https://in.indeed.com/B-Tech-Internship-jobs?vjk=8f51acd1f3df1dbe','https://internshala.com/internships/engineering-internship/','https://in.linkedin.com/jobs/data-science-intern-jobs?trk=expired','https://skilloutlook.com/career-corner/four-iits-announce-summer-research-internship-programs-2023-for-university-students ']
for url in urls:
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    links = soup.find_all('a')
    #print(links)
    #print("soup=",soup.text.split(" "))
