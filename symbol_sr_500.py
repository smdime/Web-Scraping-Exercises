import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

response = requests.get(url)

t = response.text

soup = BeautifulSoup(t,features="html.parser")

# finalSymbol = "ZTS"
trs = soup.find_all("tr")

symbols = []

for i in range(len(trs)):
    # looping through the data, but not including index 0, which is the header name 'Symbol'
    if i != 0:
        symbol = trs[i].contents[1].text.strip() #stripping off the newline
        symbols.append(symbol)
        if len(symbols) == 503:
            break

print(symbols)