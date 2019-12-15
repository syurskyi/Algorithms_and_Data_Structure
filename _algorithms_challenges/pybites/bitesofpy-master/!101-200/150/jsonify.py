import json
import re

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""


def convert_to_json(members=members):
    r = re.compile(r'(?P<id>\d+)[,|;](?P<first_name>\w+)[,|;](?P<last_name>\w+)[,|;](?P<email>.*)')
    result = [r.match(line).groupdict() for line in members.splitlines(keepends=False)[2:]]
    return json.dumps(result)
