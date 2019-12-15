from collections import Counter
from difflib import SequenceMatcher
from itertools import product
import re

# These were given
IDENTICAL = 1.0
TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
# ^ searches for a string; ^< means don't include '<'
# + means to search for this pattern 1 or more times


def get_tags():
    """
    Find all tags (TAG_HTML) in RSS_FEED.
    Replace dash with whitespace.
    Hint: use TAG_HTML.findall
    """
    with open(RSS_FEED, 'r') as file:
        tags = TAG_HTML.findall(file.read())
        tags = [re.sub('[-]', ' ', tag.lower()) for tag in tags]

    return tags


def get_top_tags(tags=get_tags(), n=10):
    """
    :param: list of tags, as read in by get_tags()
    Get the TOP_NUMBER of most common tags
    Hint: use most_common method of Counter (already imported)
    """
    return Counter(tags).most_common(n)


def get_similarities(tags=get_tags()):
    """
    Find set of tags pairs with similarity ratio of > SIMILAR
    Hint 1: compare each tag, use for in for, or product from itertools
    (already imported)
    Hint 2: use SequenceMatcher (imported) to calculate the similarity ratio
    Bonus: for performance gain compare the first char of each tag in pair
    and continue if not the same
    """
    # similar_tags = {}
    # for tag in tags:
    #     for other_tag in tags:
    #         if tag[0] is not other_tag[0]: continue
    #         similarity = SequenceMatcher(None, tag, other_tag).ratio()
    #         if SIMILAR < similarity < 1.0:
    #             if similar_tags.get(tag) is None:
    #                 similar_tags[tag] = [other_tag]
    #             elif other_tag in similar_tags[tag]: continue
    #             else: similar_tags[tag].append(other_tag)


# Much more elegant solution
    for pair in product(tags, tags):
        if pair[0][0] != pair[1][0]: continue
        similarity = SequenceMatcher(None, *pair).ratio()
        pair = tuple(sorted(pair))
        if SIMILAR < similarity < 1.0:
            yield pair


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
