import requests
import pandas as pd
url = "http://webscraper.io/test-sites/tables"

response = requests.get(url, verify=False)
#print(response.text)#Always visualizing our progress
#Each value in the table is surrounded by <tr> </tr>
tables = response.text.split("<tr>")
counter = 0

for table in tables:
    if "Mark" in table:#Seeing where data tarts
        print("Mark:",counter)
    if "@twitter" in table:#Seeing where data ends
        print("Twitter:",counter)
    counter+=1
    
tables = tables[2:19] #Reducing our data down to what's interesting
#print(tables)#Always visualizing our progress
reducedTables = []
for table in tables:
    if "<td>" in table:
        reducedTables.append(table)
#print(reducedTables)#Always visualizing our progress

doubleReducedTables = []
for table in reducedTables:
    temp = table.split("<td>")
    for tableTemp in temp:
        if "</td>" in tableTemp:
            #Here we make the first part of the string be the #, name, last name, username
            doubleReducedTables.append(tableTemp) 
#print(doubleReducedTables)#Always visualizing our progress
#To store out data in a neat fashion
data = {"#":[],
        "First Name":[],
        "Last Name":[],
        "Username":[]}
for i in range(len(doubleReducedTables)):
    table = doubleReducedTables[i]
    t = i%4 #Cycling over 4 different values
    value = table.split("</td>")[0]
    #Our data is always before the </td> value, so the first element after the split
    if value != "-":#We can take out the empty line
        if t == 0:
            data["#"].append(value)
        elif t == 1:
            data["First Name"].append(value)
        elif t == 2:
            data["Last Name"].append(value)
        elif t == 3:
            data["Username"].append(value)
    
df = pd.DataFrame(data)
print(df)