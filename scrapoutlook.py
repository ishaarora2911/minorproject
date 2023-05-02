import re
import requests
from bs4 import BeautifulSoup
url = "https://skilloutlook.com/career-corner/four-iits-announce-summer-research-internship-programs-2023-for-university-students/"
#proxy = ['']
headers = {"User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
#print(response.text)
print(soup.title)
li = []
li2 = []
li3 = []

for i in soup.find_all('div', id='entryContainer'):
    for link in i.find_all('a',
                           attrs={'href': re.compile("^https://skilloutlook.com/")}):
        li.append(link.get('href'))

        print(li)
# for j in range(0, len(li)):
#     i = li[j]
#     # print("link=",i)
#     url2 = i
#     headers = {
#         "User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}
#     response2 = requests.get(url2, headers=headers,proxies={"https":proxy,"https":proxy})
#     soups = BeautifulSoup(response2.text, "html.parser")
#     for j in soups.find_all('div', id='entryContainer'):
#         for data in j.find_all('p'):
#             data = data.text
#             new_text = ''
#             # Removing special characters from string
#             original_string = data
#             processed_string = re.sub(r'[^\w\s]', '', original_string)
#             #    print(processed_string)
#             li2.append(processed_string)
#             str1 = ""
#
#             # traverse in the string
#             for ele in li2:
#                 str1 += ele
#
#             # return string
#            # print(str1)
#
#     li3.append(str1)
#     li2=[]
#     str1 = " "
# print(li3)
# #print(li3[0])
# #print(li3[1])
# # print(li3[2])
# # print(li3[3])
# # print(li3[4])
# # print(len(li3))
# # print(type(li3))
#
