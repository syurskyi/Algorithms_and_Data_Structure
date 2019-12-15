import re

from text2cols import text_to_columns


def test_text_to_one_col():
    text = """My house is small but cosy."""
    expected = [
        r"^My house is small",
        r"^but cosy."
    ]
    output = text_to_columns(text).split("\n")
    for line, match in zip(output, expected):
        assert re.search(match, line)


def test_text_to_two_cols():
    text = """My house is small but cosy.

    It has a white kitchen and an empty fridge."""
    expected = [
        r"^My house is small\s+It has a white",
        r"^but cosy\.\s+kitchen and an empty",
        r".*fridge."
    ]
    output = text_to_columns(text).split("\n")
    for line, match in zip(output, expected):
        assert re.search(match, line)


def test_text_to_three_cols():
    text = """My house is small but cosy.

    It has a white kitchen and an empty fridge.

    I have a very comfortable couch, people love to sit on it."""
    expected = [
        r"^My house is small\s+It has a white\s+I have a very",
        r"^but cosy\.\s+kitchen and an empty\s+comfortable couch,",
        r".*fridge\.\s+people love to sit",
        r".*on it."
    ]
    output = text_to_columns(text).split("\n")
    for line, match in zip(output, expected):
        assert re.search(match, line)


def test_text_to_four_cols():
    text = """My house is small but cosy.

    It has a white kitchen and an empty fridge.

    I have a very comfortable couch, people love to sit on it.

    My mornings are filled with coffee and reading, if only I had a garden"""

    expected = [
        r"^My house is small\s+It has a white\s+I have a very\s+My mornings are",
        r"^but cosy\.\s+kitchen and an empty\s+comfortable couch,\s+filled with coffee",
        r".*fridge\.\s+people love to sit\s+and reading, if only",
        r".*on it\.\s+I had a garden",
    ]
    output = text_to_columns(text).split("\n")
    for line, match in zip(output, expected):
        assert re.search(match, line)