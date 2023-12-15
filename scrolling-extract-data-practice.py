from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
from bs4 import BeautifulSoup

url = "https://www.google.com"

options = Options()
# to keep the browser open after the script finishes
options.add_experimental_option("detach", True) 

driver = webdriver.Edge(options=options)
driver.maximize_window()
driver.get(url)

search = "data analyst"
search_bar = driver.find_element(By.ID,"APjFqb")
search_bar.send_keys("data analyst")
search_bar.send_keys(Keys.RETURN)

# Wait for the page to load
time.sleep(5)

# # Filter by jobs
# jobs_button = driver.find_element(By.XPATH,'//*[@id="search-reusables__filters-bar"]/ul/li[1]/button')
# jobs_button.click()

# Scroll down a specific frame
scroll = driver.find_element(By.ID,'rcnt')
# Scroll the element into view
#(SCROLL ONCE BUT NOT THROUGH END) driver.execute_script("arguments[0].scrollIntoView();", scroll)
#(SCROLL ONCE BUT NOT THROUGH END) driver.execute_script("window.scrollTo(0, arguments[0].offsetTop);", scroll)
#(WORKS FOR NOT FOR ENDLESS PAGES) driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#(SCROLL FOR ENDLESS SCROLLING)
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # pause to allow loading of new content
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:  # check if the page height has remained the same
        break  # we've reached the end of the page
    last_height = new_height

time.sleep(5)

#using BeautifulSoup

soup = BeautifulSoup(driver.page_source,features="html.parser")

results = {
    "Title": [],
    "Link": []
}

searches = soup.find_all("a")
for search in searches:
    href = search.get('href')
    if href and href.startswith('https://') and 'google.com' not in href:
        # Find the closest h3 tag associated with the current link
        title = search.find_next('h3')  # You can adjust the method based on your HTML structure
        
        if title:
            results["Title"].append(title.text)
            results["Link"].append(href)

df = pd.DataFrame(results)
df.to_csv("data-analyst-search-results.csv")
print(df)
