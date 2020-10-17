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

def arrange_url(my_string):
    """
    site urlsinin yorumlar url ine convert etmek
     için kullanılan function
    """
    temp_string = ""
    counter = 0;
    for i in my_string:
        if (i == "?" and counter == 0):
            i = i.replace("?" , "/yorumlar?")
            counter = counter + 1
        temp_string = temp_string + i 
    return temp_string


#Part-1 SELENİUM ----------------------------------------------------------
#Neccss
PATH = "C:\webdrivers\chromedriver.exe"

#user-agent options
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("user-agent=mertse7en7@gmail.com    ---- New-Grad Students trying to have start-up")


driver = webdriver.Chrome(options=opts, executable_path=PATH)
driver.get("https://www.trendyol.com/")

search = driver.find_element_by_class_name("search-box")
search.clear()
search.send_keys("razor mouse")
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME , "p-card-img")))
    element.click()
    my_url = driver.current_url
finally:
    #print("i cannot find")
    driver.quit()


print("Url has fetched succesfully!!!!! The URL is :{} ".format(my_url))
print("2nd phase is starting!!!")

### PART-2 BS4 ------------------------------------------------------------

#eğer ürün'de hiç ürün yoksa sıkıtnı onu check etmen gerekiyo
url = my_url
url = arrange_url(url)


source = requests.get(url).text
soup = BeautifulSoup(source , "lxml")

text = []
authors = []

"""review_module = soup.find("li" , attrs={"class" : "comment"})
direct_comment = review_card.find("p")"""
"""print(direct_comment.text)"""

review_module = soup.find("div" , attrs={"class":"pr-rnr-com-w"})
review_submodule = review_module.find("div",attrs={"class" : "rnr-com-w"})



for review_card in review_module.find_all("div" , attrs={"class" : "rnr-com-tx"}):
    text.append(review_card.text)
    authors.append("******")

df = pd.DataFrame(list(zip(authors , text)),
				columns = ["Users" , "Comments"])

"""import os
print(os.getcwd())
print(authors)
"""

df.to_excel("comment-trendyol.xlsx")


