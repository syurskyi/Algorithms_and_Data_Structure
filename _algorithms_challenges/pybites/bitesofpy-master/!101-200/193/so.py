import requests
from bs4 import BeautifulSoup

cached_so_url = 'https://bit.ly/2IMrXdp'


def load_page(url):
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(url).content.decode('utf-8')


def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    content = load_page(url)
    soup = BeautifulSoup(content)
    questions = [(question.select_one('a.question-hyperlink').string.strip(),
                  int(question.select_one('span.vote-count-post').string.strip()))
                 for question in soup.find_all(class_='question-summary')
                 if question.select_one('div.views').string.strip().endswith('m views')]
    return sorted(questions, key=lambda x: -x[1])
