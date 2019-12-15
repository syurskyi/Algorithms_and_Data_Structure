from Previous.rrhood import make_character_index


the_neetle_tree = """
There were once two brothers who lived on the edge of a forest.
The elder brother was very mean to his younger brother and ate up all the food and took all his good clothes.
One day, the elder brother went into the forest to find some firewood to sell in the market.
As he went around chopping the branches of a tree after tree, he came upon a magical tree.
The tree said to him, ‘Oh kind sir, please do not cut my branches.
If you spare me, I will give you my golden apples’.
The elder brother agreed but was disappointed with the number apples the tree gave him.
Greed overcame him, and he threatened to cut the entire trunk if the tree didn’t give him more apples.
The magical tree instead showered upon the elder brother hundreds upon hundreds of tiny needles.
The elder brother lay on the ground crying in pain as the sun began to lower down the horizon.
The younger brother grew worried and went in search of his elder brother.
He found him with hundreds of needles on his skin.
He rushed to his brother and removed each needle with painstaking love.
After he finished, the elder brother apologised for treating him badly and promised to be better.
The tree saw the change in the elder brother’s heart and gave them all the golden apples they could ever need.
"""
characters = ('elder brother', 'younger brother', ('the tree', 'magical tree'))


def test_make_character_index_with_default_args():
    keys = ('red riding hood', 'grandmother', 'wolf', 'woodsman')
    values = (
        [1, 2, 3, 6, 7, 8, 11, 18, 19, 21, 24, 26, 28, 30, 33, 36],
        [2, 3, 5, 11, 12, 14, 15, 16, 17, 21, 22, 24, 26, 28, 30, 33, 36],
        [9, 10, 13, 14, 16, 17, 18, 20, 23, 25, 27, 29, 30, 31, 33, 35],
        [32, 34, 35]
    )
    expected = dict(zip(keys, values))
    actual = make_character_index()
    assert actual == expected


def test_make_character_index_with_other_args():
    keys = ('elder brother', 'younger brother', 'the tree')
    values = (
        [2, 3, 7, 9, 10, 11, 14, 15],
        [2, 11],
        [4, 5, 7, 8, 9, 15],
    )
    actual = make_character_index(text=the_neetle_tree,
                                  characters=characters)
    expected = dict(zip(keys, values))
    assert actual == expected