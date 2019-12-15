
from bs4 import BeautifulSoup
import requests
import string

nytimes_html = requests.get('http://www.nytimes.com/').text

soup = BeautifulSoup(nytimes_html, 'html.parser')
filename = input("Enter a filename: ")

with open(filename, 'w') as open_file:
    for story_heading in soup.find_all(class_="story-heading"):
        if story_heading.a:
            open_file.write(str(story_heading.a.text.replace("\n", " ").strip().encode('utf-8')))
        else:
            open_file.write(str(story_heading.contents[0].strip().encode('utf-8')))
