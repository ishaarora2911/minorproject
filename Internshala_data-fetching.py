import requests
import random
import time
# time.sleep(1)
from bs4 import BeautifulSoup
url = "https://internshala.com/internships/engineering-internship/"
proxy_list=[ 'http://68.132.12.228:8888',
          'http://200.105.215.22:33630',
         'http://14.32.161.114:8080',
        'http://152.228.206.188:80',
       'http://45.61.187.67:4007',
         'http://103.42.180.24:45787'
          ]
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
]

headers = {"User-Agent": random.choice(user_agent_list)}
proxy=random.choice(proxy_list)
response = requests.get(url, headers=headers,proxies={"https":proxy,"htttps":proxy})
#print(response)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.text)
# for i in soup.find_all('div', class_="internship_list_container"):
#     print(i.text)
# for i in soup.find_all('div', id="internship_list_container"):
#     print(i.text)
for i in soup.find_all('div', class_="container-fluid individual_internship visibilityTrackerItem"):
     print(i.text)


