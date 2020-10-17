#selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#bs4
import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd

#Neccss
PATH = "C:\webdrivers\chromedriver.exe"

#user-agent options
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("user-agent=mertse7en7@gmail.com    ---- New-Grad Students trying to have start-up")



driver = webdriver.Chrome(options=opts, executable_path=PATH)
driver.get("https://www.hepsiburada.com/")

# Search
search = driver.find_element_by_class_name("desktopOldAutosuggestTheme-input")
search.clear()
search.send_keys("Galaxy note")
search.send_keys(Keys.RETURN)

try :
    element = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.CLASS_NAME , "hb-pl-cn")))
    element.click()
    my_url = driver.current_url
finally:
    print("I think i can not see")
    driver.quit()

print(my_url)
print("2nd phase is starting!!!")

source = requests.get(my_url).text
soup = BeautifulSoup(source , "lxml")

text = []
authors = []

rewiev_module = soup.find("div",attrs={"class" : "paginationContentHolder"})
review_card =rewiev_module.find("div",attrs={"class" : "ReviewCard-module-34AJ_"})

for review_card in rewiev_module.find_all("div",attrs={"class" : "ReviewCard-module-34AJ_"}):
    yazilar = review_card.find("span",itemprop ="description").text
    author = review_card.find("span" , itemprop = "author").text
    text.append(yazilar)
    authors.append(author)

df = pd.DataFrame(list(zip(authors , text)),columns = ["Users" , "Comments"])


df.to_excel("comment-hepsiburada4.xlsx")





























