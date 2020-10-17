"""https://www.trendyol.com/sony/playstation-4-slim-1-tb-turkce-menu-2-ps4-kol-p-4836588?boutiqueId=532766&merchantId=151245

https://www.trendyol.com/sony/playstation-4-slim-1-tb-turkce-menu-2-ps4-kol-p-4836588/yorumlar?boutiqueId=532766&merchantId=151245""" 
### 4836588 "/yorumlar" eklencek araya

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

#eğer ürün'de hiç ürün yoksa sıkıtnı onu check etmen gerekiyo
url ="https://www.trendyol.com/haylou/t15-kablosuz-bluetooth-kulaklik-2200-mah-yuksek-pil-gucu-p-38879372?boutiqueId=531528&merchantId=133183"
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