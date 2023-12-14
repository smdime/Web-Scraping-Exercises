import requests
from bs4 import BeautifulSoup
import pandas as pd
import time,os.path,datetime

# Make it run every 15 seconds
# check if our file exists to not overwrite it
# Add an additional field to track when the data was collected


def main():
    while True:
        #Check current time
        start = time.time()
        waitTime = 150

        #Extract and Save data
        data = {"symbol":[],
                "metric":[],
                "value":[],
                "time":[]}

        try:
            symbols = getCompanyList()
        except Exception as e:
            print(str(e))
            time.sleep(waitTime)

        for symbol in symbols:
            try:
                names,values = getFinancialInformation(symbol)
            except:
                continue
            collectedTime = datetime.datetime.now().timestamp()
        

            for i in range(len(names)):
                data["symbol"].append(symbol)
                data["metric"].append(names[i])
                data["value"].append(values[i])
                data["time"].append(collectedTime)

        currentDate = datetime.date.today()
        df = pd.DataFrame(data)
        savePath = str(currentDate) + "financialData.csv"
        if os.path.isfile(savePath):
            #don't overwrite
            df.to_csv(savePath,mode="a",header=False,columns=["symbol","metric","value","time"])
        else:
            #create
            df.to_csv(savePath,columns=["symbol","metric","value","time"])
        
        
        #Wait until 15 seconds have passed from above
        timeDiff = time.time()-start
        if 15-timeDiff > 0: #if the program runs for a long time
            time.sleep(15-timeDiff)


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
