#again a web scraping and write to a file


import requests

from bs4 import BeautifulSoup

url =  'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
html_object = requests.get(url)

html_text = html_object.text


print html_text

soup = BeautifulSoup(html_text)

article_graph_list = soup.select("div.article-main p")
article_text_list = [p.get_text() for p in article_graph_list]
title = soup.h1.get_text()

print title, "\n"
article_content =  "\n\n".join(article_text_list).encode('utf-8').strip()
print article_content

#with closes the file immediately after writing
with  open("article_content_scraped_2.txt",'w') as file_object:
	file_object.write(title+"\n")
	file_object.write(article_content)



