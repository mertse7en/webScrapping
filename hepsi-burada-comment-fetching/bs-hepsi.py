import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd

url ="https://www.hepsiburada.com/monopoly-yeni-piyon-serisi-c1009-p-OYUNHSBR00009"

source = requests.get(url).text
soup = BeautifulSoup(source , "lxml")

text = []
authors = []



rewiev_module = soup.find("div",attrs={"class" : "paginationContentHolder"})
review_card =rewiev_module.find("div",attrs={"class" : "ReviewCard-module-34AJ_"})
#print(rewiev_module.prettify())

yazilar = review_card.find("span",itemprop ="description").text
#print(yazilar)


## okey şimdi aynısın hepsi için deniycem
for review_card in rewiev_module.find_all("div",attrs={"class" : "ReviewCard-module-34AJ_"}):
	#print(rewiev_module.prettify())
	yazilar = review_card.find("span",itemprop ="description").text
	author = review_card.find("span" , itemprop = "author").text
	text.append(yazilar)
	authors.append(author)

df = pd.DataFrame(list(zip(authors , text)),
				columns = ["Users" , "Comments"])

import os
print(os.getcwd())
print(authors)


df.to_excel("commenttt.xlsx")
