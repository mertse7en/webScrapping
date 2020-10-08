
import requests
from bs4 import BeautifulSoup
import re


with open ("simple.html") as html_file:
	soup = BeautifulSoup(html_file,"lxml")

article = soup.find("div",attrs = {"class":"article"})
#print(article)

headline = article.h2.a.text
print(headline)

print("-"*20)

texts = article.p.text
print(texts)

print("*"*20)

## eğer Find_all kullanırsam bütün divlerin istini getiriyobizde loop yapabiliyoru
#what i mean is tat

for article in soup.find_all("div",attrs = {"class":"article"}):
	headline = article.h2.a.text
	print(headline)

	print("-"*20)

	texts = article.p.text
	print(texts)

	print("")