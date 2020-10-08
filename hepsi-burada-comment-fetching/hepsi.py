import requests
from bs4 import BeautifulSoup
import re
import csv

url ="https://www.hepsiburada.com/sony-playstation-4-ps4-slim-500-gb-oyun-konsolu-eurasia-garantili-pm-HB0000018CDU-yorumlari"

source = requests.get(url).text
soup = BeautifulSoup(source , "lxml")




rewiev_module = soup.find("div",attrs={"class" : "paginationContentHolder"})
review_card =rewiev_module.find("div",attrs={"class" : "ReviewCard-module-34AJ_"})
#print(rewiev_module.prettify())

yazilar = review_card.find("span",itemprop ="description").text
#print(yazilar)


## okey şimdi aynısın hepsi için deniycem
for review_card in rewiev_module.find_all("div",attrs={"class" : "ReviewCard-module-34AJ_"}):
	#print(rewiev_module.prettify())
	yazilar = review_card.find("span",itemprop ="description").text
	print(yazilar)
	print("-"*30)