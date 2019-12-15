#use the beautiful soup library and print all the titles on the new york times page

import string
import requests
from bs4 import BeautifulSoup

#using request library get request the page from NYT and print the text
url = 'https://www.nytimes.com/'

html_object = requests.get(url)

text_html = html_object.text
#print html_object #has the response 200 msg
#print text_html


#now use the beautiful soup to print all the titles. it takes in a text html as arg

soup = BeautifulSoup(text_html) #instantiating the object soup using class BS

#get all the titles and format and print it
for story_heading in soup.find_all(class_="story-heading"):
	if story_heading.a:
		print story_heading.a.text.replace("\n"," ").strip()
	else: 
       		print story_heading.contents[0].strip()


