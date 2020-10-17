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
driver.get("https://www.n11.com/")

search = driver.find_element_by_id("searchData")
search.clear()
search.send_keys("ps4")
search.send_keys(Keys.RETURN)

try :
    element = WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.CLASS_NAME , "columnContent ")))
    element.click()
    my_url = driver.current_url
finally:
    print("I think its OK!")
    driver.quit()

print("Url has fetched succesfully!!!!! The URL is :{} ".format(my_url))
print("2nd phase is starting!!!")

### 2nd PART ------------------------------------------


url = my_url
added_str = "#unf-review"

#comment urls add with #unf-review
url = url + added_str

source = requests.get(url).text
soup = BeautifulSoup(source , "lxml")

text = []
authors = []

for review_card in soup.find_all("li" , attrs={"class" : "comment"}):
    #print(rewiev_module.prettify())
	yazilar = review_card.find("p").text
	author = review_card.find("span" , attrs = {"class" : "userName"}).text
	text.append(yazilar)
	authors.append(author)

df = pd.DataFrame(list(zip(authors , text)),
				columns = ["Users" , "Comments"])

"""import os
print(os.getcwd())
print(authors)
"""

df.to_excel("comment-n11-2.xlsx")