import requests
from bs4 import BeautifulSoup
import time
time.sleep(1)
proxy={ 'http': 'http://135.181.137.85:3128'}
url = "https://www.wayup.com/s/internships/summer/"
headers={"User-Agent":  "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko"}
response = requests.get(url, headers=headers,proxies=proxy,timeout=10)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.text)