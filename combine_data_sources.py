import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    data = {"symbol":[],
            "metric":[],
            "value":[]}

    symbols = getCompanyList()
    for symbol in symbols:
        names,values = getFinancialInformation(symbol)

        for i in range(len(names)):
            data["symbol"].append(symbol)
            data["metric"].append(names[i])
            data["value"].append(values[i])

        # data["symbol"] += [symbol]*len(names)
        # data["metric"] += names
        # data["values"] += values

    df = pd.DataFrame(data)
    df.to_csv("financialData.csv")
    

def getFinancialInformation(symbol):
    url = "https://finance.yahoo.com/quote/"+symbol+"?p="+symbol

    response = requests.get(url)

    t = response.text

    soup = BeautifulSoup(t,features="html.parser")

    finalName = "1y Target Est"
    trs = soup.find_all("tr")

    names = []
    values = []

    namVal = {}

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

    return names, values


def getCompanyList():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

    response = requests.get(url)

    t = response.text

    soup = BeautifulSoup(t,features="html.parser")

    trs = soup.find_all("tr")

    symbols = []

    for i in range(len(trs)):
        if i != 0:
            symbol = trs[i].contents[1].text.strip() #stripping off the newline
            symbols.append(symbol)
            if len(symbols) == 503:
                break

    return symbols


if __name__ == "__main__":
    main()
