from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd 


pages = []
prices = []
stars = []
titles = []
urlss = []


pages_to_scrape = 50

for i in range(1,pages_to_scrape+1):
    url = ("http://books.toscrape.com/catalogue/page-{}.html").format(i)
    pages.append(url)

for item in pages:
    page = requests.get(item)
    soup = bs4(page.text , "lxml")

    for title in soup.find_all("h3"):   
        titles.append(title.text)

    for price in soup.find_all('p', class_='price_color'):
        prices.append(price.getText())

    for s in soup.find_all('p' , class_ = 'star-rating'):
        for k,v in s.attrs.items():
            stars.append(v[1])

    dive = container = soup.find_all("div", class_="image_container")

    for thumbs in dive :
        tgs = thumbs.find('img' , class_="thumbnail")
        urls = "books.toscrape.com/" +str(tgs["src"])
        urlss.append(urls)

df2 = pd.DataFrame(list(zip(titles, prices , stars)), 
               columns =['Titles', 'prices','stars'])
df2["image-link"] = urlss

import os
print(os.getcwd())

#df2.to_excel(r"C:\Users\MERT\Desktop\bs-deneme\bookstore-fetching\ready_datasett2.xlsx")
