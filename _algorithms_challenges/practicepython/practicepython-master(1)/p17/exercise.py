'''
The following is a mostly-correct solution that is +99 percent the
website author's. I had a lot of issues coming up with a correct
solution but was on the right track in looking for the
'class="story-heading"' bit. I had a lot of problems handling unicode
characters, which was not discussed. I added the encode lines to handle it.
Though I'm not sure if it is my Python environment, console, or maybe something else...

'''



from bs4 import BeautifulSoup
import requests
import string

nytimes_html = requests.get('http://www.nytimes.com/').text

soup = BeautifulSoup(nytimes_html, 'html.parser')

for story_heading in soup.find_all(class_="story-heading"):
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip().encode('utf-8'))
    else:
        print(story_heading.contents[0].strip().encode('utf-8'))
