import re
def abbreviate(words):
    
    return "".join(map(lambda x: x[0].upper(), re.findall(r"[a-zA-Z']+", words)))
