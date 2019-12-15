import sys
from urllib.parse import urlparse

INTERNAL_LINKS = ('pybit.es', 'codechalleng.es')


def make_html_links():
    for line in sys.stdin:
        res = process_line(line)
        if res and len(res.strip()) > 0:
            print(res)


def process_line(line):
    if line.startswith('http'):
        url, *title = [l.strip() for l in line.split(',')]
        if len(title) > 1:
            return ''
        title = title[0]
        elements = urlparse(url)
        if elements.hostname not in INTERNAL_LINKS:
            target = ' target="_blank"'
        else:
            target = ''
        return f'<a href="{url}"{target}>{title}</a>'  # .encode('ascii')
    return ''


if __name__ == '__main__':
    make_html_links()
