import requests
from bs4 import BeautifulSoup
import re
import csv
import pandas as pd



url ="https://www.n11.com/urun/samsung-galaxy-m21-duos-64-gb-samsung-turkiye-garantili-1481543?magaza=samsungturkiye"
added_str = "#unf-review"

#comment urls add with #unf-review
url = url + added_str

source = requests.get(url).text
soup = BeautifulSoup(source , "lxml")

text = []
authors = []

"""review_module = soup.find("li" , attrs={"class" : "comment"})
direct_comment = review_card.find("p")"""
"""print(direct_comment.text)"""

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

df.to_excel("comment3.xlsx")