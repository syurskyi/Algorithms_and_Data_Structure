import pytest

from improved_xmas_tree import generate_improved_xmas_tree

default_tree = """
         +
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
    |||||||||||
    |||||||||||
"""
smaller_tree = """
  +
  *
 ***
*****
 |||
 |||
"""


@pytest.mark.parametrize("size, expected", [(10, 13), (5, 8), (20, 23)])
def test_height_xmas_tree(size, expected):
    actual = len(generate_improved_xmas_tree(size).rstrip().splitlines())
    assert actual == expected


@pytest.mark.parametrize("size, expected", [(3, 9), (5, 25), (20, 400)])
def test_num_leafs_used(size, expected):
    assert generate_improved_xmas_tree(size).count("*") == expected


@pytest.mark.parametrize("size, expected", [(3, 1), (5, 1), (20, 1)])
def test_star_used(size, expected):
    assert generate_improved_xmas_tree(size).count("+") == expected


@pytest.mark.parametrize("size, expected", [(3, 6), (5, 10), (20, 42)])
def test_trunk_used(size, expected):
    assert generate_improved_xmas_tree(size).count("|") == expected


def test_outputs():
    actual_tree = generate_improved_xmas_tree().strip("\n").split("\n")
    expected_tree = default_tree.strip("\n").split("\n")
    for i, j in zip(actual_tree, expected_tree):
        assert i.rstrip() == j.rstrip()

    actual_tree = generate_improved_xmas_tree(3).strip("\n").split("\n")
    expected_tree = smaller_tree.strip("\n").split("\n")
    for i, j in zip(actual_tree, expected_tree):
        assert i.rstrip() == j.rstrip()