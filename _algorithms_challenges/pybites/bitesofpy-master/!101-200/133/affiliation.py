def generate_affiliation_link(url):
    pos = url.find('/dp/')
    return f'http://www.amazon.com{url[pos:pos + 14]}/?tag=pyb0f-20'
