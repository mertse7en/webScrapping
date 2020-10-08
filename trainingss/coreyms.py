import requests
from bs4 import BeautifulSoup
import re
import csv


source = requests.get("https://coreyms.com/").text

soup = BeautifulSoup(source,"lxml")

#print(soup.prettify())

article = soup.find("article")
#print(article.prettify())

headline = article.h2.a.text
#print(headline)

print("-"*15)
# all article title

csv_file = open("cms_scrape.csv","w")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["headline","summary","video_link"])

for article in soup.find_all("article"):
	headline = article.h2.a.text
	print(headline)
	print("-"*50)




	# şimdi summaryleri alalm

	summary = article.find("div" , attrs ={"class" : "entry-content"})
	yazi = summary.p.text
	print(yazi)
	print("-"*50)

	"""#bütün yazilari alalm --> bu böyle değil sonra check edelim merto

	for summary in  article.find("div" , attrs ={"class" : "entry-content"}):
	yazi = summary.p.text
	print(yazi)
	print("*"*15)"""

	try:
		vid_src = article.find("iframe",attrs ={"class" : "youtube-player"})["src"]
		#print(vid_src)
		#print("-"*15)

		vid_src = vid_src.split("/")[4]
		#print(vid_src)
		vid_id = vid_src.split("?")[0]
		#print(vid_id)

		yt_link= f"https://youtube.com/watch?v={vid_id}"
	except:
		yt_link =None


	print(yt_link)


	print("*"*50)
	print("*"*50)

	csv_writer.writerow([headline,summary,yt_link])

print("csv writing has done")
csv_file.close()





