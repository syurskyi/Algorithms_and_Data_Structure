from typing import List

number_ordinals = [
    "first", "second", "third", "fourth",
    "fifth", "sixth", "seventh", "eighth",
    "ninth", "tenth", "eleventh", "twelfth"]

number_strings = [
    "a", "two", "three", "four",
    "five", "six", "seven", "eight",
    "nine", "ten", "eleven", "twelve"]

number_things = [
    "Partridge in a Pear Tree", "Turtle Doves", "French Hens",
    "Calling Birds", "Gold Rings", "Geese-a-Laying",
    "Swans-a-Swimming", "Maids-a-Milking", "Ladies Dancing",
    "Lords-a-Leaping", "Pipers Piping", "Drummers Drumming"]

def recite(start_verse: int, end_verse: int) -> List[str]:
    lyrics = []
    for i in range(start_verse, end_verse + 1):
        lyrics.append(f"On the {number_ordinals[i - 1]} day of Christmas my true love gave to me: {concate_things(i)}")
    return lyrics

def concate_things(num: int) -> str:
    results: List[str] = []
    for i in range(num):
        results.insert(0, f"{number_strings[i]} {number_things[i]}")

    if num > 1:
        results[-1] = "and " + results[-1]
    
    return ", ".join(results) + "."
