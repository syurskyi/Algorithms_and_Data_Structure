#decode a wbpage using beautiful soup and request library


from bs4 import BeautifulSoup
import requests

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'

html_object = requests.get(url)

html_text = html_object.text


#print html_text #text html is printed successfully



soup = BeautifulSoup(html_text) # create an instance of beautiful soup using html text got

for story_headline in soup.find_all(class_="content drop-cap"):
        if story_headline.p:
                print story_headline.p
        
article_graph_list = soup.select("div.article-main p")
article_text_list = [p.get_text() for p in article_graph_list]
title = soup.h1.get_text()

print title, "\n"
article_content =  "\n\n".join(article_text_list).encode('utf-8').strip()
print article_content

file_object = open("article_content_scraped.txt",'w')
file_object.write(title+"\n")
file_object.write(article_content)
file_object.close()

