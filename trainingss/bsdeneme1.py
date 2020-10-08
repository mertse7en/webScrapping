"""

-go to website
-get source code inside of bs module
-parse the html code with using Bs module

"""


import requests
from bs4 import BeautifulSoup
import re


#bi request yaptım siteye
r = requests.get("https://tr.aliexpress.com/item/32219559084.html?spm=a2g10.search0306.3.4.42d429748H0GFT&ws_ab_test=searchweb0_0,searchweb201602_0,searchweb201603_0,ppcSwitch_0&algo_pvid=99b6630d-761e-44af-bcea-30dcf467e4cc&algo_expid=99b6630d-761e-44af-bcea-30dcf467e4cc-0#feedback")
#contenti alıp lxmle parse ettim
soup = BeautifulSoup(r.content , "lxml")

#p_list = soup.find_all("p")
#print(soup)


coms = soup.find_all("div",attrs = {"class":"buyer-feedback"})
print



for tag in soup.find_all(re.compile("t")):
    print(tag.name)