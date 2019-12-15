import pytest
from corpora import GETTYSBURG, Corpora

# https://www.oaktreecapital.com/insights/howard-marks-memos
TAX_SYSTEM_IN_US = """Suppose that every day, ten men go out for beer, and the bill for all ten comes to $100.  If they paid their bill the way we pay our taxes (by taxpayer decile), it would go something like this:

The first four men (the poorest) would pay nothing.
The fifth would pay $1.
The sixth would pay $3.
The seventh would pay $7.
The eighth would pay $12.
The ninth would pay $18.
The tenth man (the richest) would pay $59.

So, that’s what they decided to do.

The ten men drank in the bar every day and seemed quite happy with the arrangement, until one day, the owner threw them a curve ball.  “Since you’re all such good customers,” he said, “I’m going to reduce the cost of your daily beer by $20.”  Drinks for the ten men would now cost just $80.

The group still wanted to pay their bill the way we pay our taxes.  So the first four men were unaffected. They would still drink for free.  But what about the other six?  How could they divide up the $20 windfall so that everyone would get his fair share?

The bar owner suggested that it would be fair to reduce each man’s bill by a higher percentage the poorer he was, to follow the principle of the tax system they had been using, and he proceeded to suggest the new lower amounts each should now pay.

And so the fifth man, like the first four, now paid nothing (a 100% saving).
The sixth now paid $2 instead of $3 (a 33% saving).
The seventh now paid $5 instead of $7 (a 29% saving).
The eighth now paid $9 instead of $12 (a 25% saving).
The ninth now paid $14 instead of $18 (a 22% saving).
The tenth now paid $50 instead of $59 (a 15% saving).

The first four continued to drink for free, and the latter six were all better off than before.  But, once outside the bar, the men began to compare their savings.

“I only got a dollar out of the $20 saving,” declared the fifth man.  He pointed to the tenth man, “But he got $9!”

“Yeah, that’s right,” exclaimed the sixth man.  “I only saved a dollar, too. It’s unfair that he saved nine times more than me!”

“That’s true!” shouted the seventh man.  “Why should he get $9 back, when I got only $2?  The wealthy get all the breaks!”

“Wait a minute,” yelled the first four men in unison, “we didn’t get anything at all.  This new tax system exploits the poor!”

The nine men surrounded the tenth and beat him up.

The next day, the tenth man didn’t show up, so the other nine sat down and had their beers without him.  But when it came time to pay the bill, they discovered something important: They didn’t have enough money between all of them for even half of the bill!

And that is how our tax system works.  The people who already pay the highest taxes will naturally get the most benefit from a tax reduction.  Tax them too much, attack them for being wealthy, and they just may not show up anymore.  In fact, they might start drinking overseas, where the atmosphere is friendlier."""
EXTRA_CHAR = ["—", "\n", "  "]


@pytest.fixture
def getty():
    return Corpora(GETTYSBURG)


@pytest.fixture
def beer_tax():
    return Corpora(TAX_SYSTEM_IN_US)


def test_cleanup_text(getty):
    cleaned = getty.cleaned
    assert len(cleaned) == 1419
    for char in EXTRA_CHAR[:2]:
        assert char in cleaned


def test_cleanup_text_one_extra_char(getty):
    getty.extra = [EXTRA_CHAR[0]]
    cleaned = getty.cleaned
    assert len(cleaned) == 1419
    assert EXTRA_CHAR[0] not in cleaned
    assert EXTRA_CHAR[1] in cleaned


def test_cleanup_text_multiple_extra_char(getty):
    getty.extra = EXTRA_CHAR
    cleaned = getty.cleaned
    assert len(cleaned) == 1416
    for char in EXTRA_CHAR:
        assert char not in cleaned


def test_cleanup_text_alt_text(beer_tax):
    cleaned = beer_tax.cleaned
    assert len(cleaned) == 2762
    assert "$" not in cleaned


def test_word_metrics_gettysburg_default(getty):
    expected = [
        ("nation", 5),
        ("dedicated", 4),
        ("great", 3),
        ("cannot", 3),
        ("dead", 3),
    ]
    assert getty.metrics == expected


def test_word_metrics_beer_tax(beer_tax):
    expected = [("pay", 13), ("would", 12), ("men", 8), ("paid", 7), ("man", 7)]
    assert beer_tax.metrics == expected


def test_word_metrics_with_word_removed(beer_tax):
    expected = [("pay", 13), ("would", 12), ("paid", 7), ("bill", 6), ("saving", 6)]
    beer_tax.extra = ["men", "man"]
    assert beer_tax.metrics == expected


def test_graph_gettysburgh(getty, capfd):
    expected = [
        "    nation #####",
        " dedicated ####",
        "     great ###",
        "    cannot ###",
        "      dead ###",
    ]
    getty.extra = EXTRA_CHAR
    getty.graph
    output = capfd.readouterr()[0].splitlines()
    assert output == expected


def test_graph_beer_tax(beer_tax, capfd):
    expected = [
        "       pay #############",
        "     would ############",
        "       men ########",
        "      paid #######",
        "       man #######",
        "      bill ######",
        "    saving ######",
        "     first #####",
        "      four #####",
        "     tenth #####",
    ]
    beer_tax.count = 10
    beer_tax.graph
    output = capfd.readouterr()[0].splitlines()
    assert output == expected


def test_graph_beer_tax_asterisk(beer_tax, capfd):
    expected = [
        "       pay *************",
        "     would ************",
        "       men ********",
        "      paid *******",
        "       man *******",
    ]
    beer_tax.tag = "*"
    beer_tax.graph
    output = capfd.readouterr()[0].splitlines()
    assert output == expected