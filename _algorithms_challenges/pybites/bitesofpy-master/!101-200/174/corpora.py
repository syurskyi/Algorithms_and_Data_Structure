import re
from collections import Counter
from dataclasses import dataclass, field
from string import punctuation
from typing import List, Set, Tuple

STOPWORDS: set = {
    "she's", "wasn", "through", "won", "that'll", "his", "once", "this",
    "you", "ll", "has", "because", "m", "ours", "doing", "any", "aren't",
    "they", "shouldn't", "being", "out", "is", "our", "it", "don", "had",
    "nor", "your", "she", "you've", "themselves", "or", "y", "needn", "on",
    "to", "at", "it's", "ve", "s", "too", "up", "didn't", "during", "haven",
    "can", "haven't", "each", "couldn", "isn't", "not", "against", "where",
    "was", "aren", "all", "by", "why", "hers", "theirs", "have", "as",
    "yourself", "their", "very", "who", "yourselves", "over", "and",
    "again", "do", "weren't", "which", "ma", "in", "such", "herself",
    "yours", "doesn", "if", "my", "after", "into", "just", "now", "isn",
    "itself", "between", "will", "other", "its", "these", "should", "re",
    "below", "having", "am", "both", "d", "you'll", "but", "should've",
    "won't", "himself", "shan't", "the", "me", "weren", "further", "until",
    "here", "myself", "whom", "were", "hasn", "don't", "wouldn't", "been",
    "before", "above", "he", "than", "most", "shan", "them", "mustn't",
    "couldn't", "you'd", "for", "of", "her", "those", "needn't", "you're",
    "t", "hadn't", "down", "o", "did", "about", "from", "does", "wouldn",
    "off", "then", "ain", "few", "hasn't", "some", "i", "ourselves", "an",
    "when", "are", "under", "more", "with", "hadn", "what", "while", "didn",
    "doesn't", "only", "him", "mightn", "be", "mightn't", "a", "how", "no",
    "there", "that", "so", "we", "same", "mustn", "wasn't", "shouldn", "own",
}
GETTYSBURG: str = """Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.

Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battlefield of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.

But, in a larger sense, we cannot dedicate—we cannot consecrate—we cannot hallow—this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us—that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion—that we here highly resolve that these dead shall not have died in vain—that this nation, under God, shall have a new birth of freedom— and that government of the people, by the people, for the people, shall not perish from the earth."""


@dataclass
class Corpora:
    """Add the inital variables along with creating any methods that
    will get this working as described in the bite's description.
    """
    txt: str
    count: int = 5
    tag: str = '#'
    extra: List[str] = field(default_factory=list)
    stopwords: Set[str] = field(init=False)

    def __post_init__(self):
        self.stopwords = STOPWORDS

    @property
    def cleaned(self) -> str:
        """Takes a corpus and cleans it up.

        * All text is made lowercase
        * All punctuations are removed
        * If a list of extract objects were given, remove those too

        :param txt: Corpus of text
        :return: cleaned up corpus
        """
        text = ''.join(c for c in self.txt.lower() if c not in punctuation)
        for x in self.extra:
            text = re.sub(x, ' ', text)
        return text

    @property
    def metrics(self) -> List[Tuple[str, int]]:
        """Generates word count metrics.

        * Using the cleaned up corpus, count up how many times each word is used
        * Exclude stop words using STOPWORDS
        * Use count to return the requested amount of the top words, defaults to 5

        :return: List of tuples, i.e. ("word", count)
        """
        wordlist = [word for word in self.cleaned.split() if not word in self.stopwords]
        metrics = Counter(wordlist)

        return metrics.most_common(self.count)

    @property
    def graph(self) -> None:
        """Generates a textual graph of the words

        * Prints out the words along with a "tag" bar graph, defaults to using
          the # character
        * The word is right-aligned and takes up 10 character spaces
        * The tag is repeated the number of counts of the word

        For example, the top 10 words in the Gettysburgh address would be
        displayed in this manner:

            nation #####
         dedicated ####
             great ###
            cannot ###
              dead ###
                us ###
             shall ###
            people ###
               new ##
         conceived ##

        :param metrics: List of tuples with word counts
        :return: None
        """
        for m in self.metrics:
            print(f'{m[0]:>10} {self.tag * m[1]}')
        return None
