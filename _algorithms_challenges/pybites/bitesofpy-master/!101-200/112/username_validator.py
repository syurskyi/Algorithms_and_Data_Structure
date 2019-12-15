# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    result = dict()
    plat = re.findall(r'(\w+)\s+Min: (\d+)\s+Max: (\d+)\s+Can contain: ([^\r\n]+)', social_platforms)
    for p in plat:
        result[p[0]] = Validator(range(int(p[1]), int(p[2])), re.compile(rf'^[{re.sub(r" ", "", p[3])}]*$'))
    return result


def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    if platform not in all_validators:
        raise ValueError
    plat = all_validators[platform]
    plat_range = len(username) in plat.range
    plat_match = plat.regex.match(username) is not None
    return plat_range and plat_match
