import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
    # Convert the table to a DataFrame
    df = pd.DataFrame(getData())
    df.to_csv('table-playground.csv', index=False)
    print(df)


def getData():
    url = "http://webscraper.io/test-sites/tables"
    response = requests.get(url, verify=False)

    t = response.text

    # Parse the HTML content
    soup = BeautifulSoup(t, 'html.parser')

    # Find the table
    trs = soup.find_all('tr')

    # print(trs[5].contents[3].text)

    data = []

    for i in range(len(trs)): #iterate inside trs
        for j in range(1): #iterate inside contents
            if i != 0 and i != 4 :
                temp_data = {
                    "#": trs[i].contents[j+1].text,
                    "first_name": trs[i].contents[j+3].text,
                    "last_name": trs[i].contents[j+5].text,
                    "username": trs[i].contents[j+7].text
                }
                data.append(temp_data)

    return data

if __name__ == "__main__":
    main()
