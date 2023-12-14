from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

url = "https://www.google.com"

options = Options()

# use the chromium version of Edge
# options.use_chromium = True

# to keep the browser open after the script finishes
options.add_experimental_option("detach", True) 

browser = webdriver.Edge(options=options)
browser.maximize_window()
browser.get(url)

inputElement = browser.find_element(By.ID,"APjFqb")
inputElement.send_keys("Yahoo Finance")
inputElement.submit() #Enter

xPath = '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a'

#search the 'Yahoo Finance' link and click
# element = browser.find_element(By.XPATH,xPath)
# element.click()

element = WebDriverWait(browser,10).until(ec.visibility_of_element_located((By.XPATH,xPath))).click()

#scroll down the page
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll down the page in a loop until the end is reached
# last_height = browser.execute_script("return document.body.scrollHeight")
# while True:
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)  # pause to allow loading of new content
#     new_height = browser.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:  # check if the page height has remained the same
#         break  # we've reached the end of the page
#     last_height = new_height


#delay before close
time.sleep(10)
browser.quit()