from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
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

time.sleep(10)

browser.quit()