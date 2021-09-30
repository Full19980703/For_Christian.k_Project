import requests
import os
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

options = webdriver.ChromeOptions()

options.add_argument("no-default-browser-check")
options.add_argument('headless')
options.add_argument('disable-dev-shm-usage')

driver = webdriver.Chrome('C:\Windows\chromedriver' , options=options)

search_key = input("Enter Search Key:")

key = str(search_key)

urls = open("urls.txt", "r")
result = open("resultUrls.txt", "w")

for url in urls:
    if len(url) == 1:
        break

    driver.get(url)
    content  = driver.page_source
    isExist = str(content).find(key)
    print(isExist)
    if isExist != -1 :
       result.write(url)

result.close()
urls.close()

os.system("resultUrls.txt")





