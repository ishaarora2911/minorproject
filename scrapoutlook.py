import re
import requests
from bs4 import BeautifulSoup
url = "https://skilloutlook.com/career-corner/four-iits-announce-summer-research-internship-programs-2023-for-university-students"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.49"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
#print(response.text)
# print(soup.title)
li=[]
li2=[]
li3=[]


for i in soup.find_all('div',id='entryContainer'):
    for link in i.find_all('a',
                          attrs={'href': re.compile("^https://skilloutlook.com/")}):
        li.append(link.get('href'))

#print(li)
for j in range(0,len(li)):
    i=li[j]
   # print("link=",i)
    url2=i
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.49"}
    response2 = requests.get(url2, headers=headers)
    soups = BeautifulSoup(response2.text, "html.parser")
    for j in soups.find_all('div',id='entryContainer'):
       for data in j.find_all('p'):

              data=data.text
      #        print(data)
              new_text = ''

              for character in data:
                  if character.isalnum():
                      new_text += character
            #  print(data.text)
              # print(type(data))

              li2.append(new_text)
              # print(len(li2))
              # print(li2)
              # str1 = ""
               # for ele in li2:
              #     str1 += ele
              # print(str1)
        #      li2=li2.split(" , "," ")
       li3.append(li2)
print(li3[0])
print(len(li3))

    #    print(li2)
    # li3.append(li2)
    # print(li3)
    # print(len(li3))





