import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AAPL?p=AAPL"

response = requests.get(url)

t = response.text

soup = BeautifulSoup(t,features="html.parser")

finalName = "1y Target Est"
trs = soup.find_all("tr")
# print(trs[0].contents[0].text)

names = []
values = []

namVal = {}
# dict2={"names":names,'values':values}

for i in range(len(trs)):
    for j in range(len(trs[i].contents)):
        if j == 0:#name
            name = trs[i].contents[j].text
            names.append(name)
        if j == 1:#value
            value = trs[i].contents[j].text
            values.append(value)
    namVal[name]=value
    if name == finalName:
        break

print(names)
print(values)
print(namVal)