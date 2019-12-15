import re

from table import (names, aliases, points, awake,
                   SEPARATOR, generate_table)

# cast to list in case of generator
table1 = list(generate_table(names))
table2 = list(generate_table(names, aliases))
table3 = list(generate_table(names, aliases, points))
table4 = list(generate_table(names, aliases, points, awake))


def test_generate_table():
    assert len(table1) == len(table2) == len(table3) == len(table4) == 6

    assert table1[0].count(SEPARATOR) == 0
    assert table2[0].count(SEPARATOR) == 1
    assert table3[0].count(SEPARATOR) == 2
    assert table4[0].count(SEPARATOR) == 3

    assert table1[1].split(SEPARATOR)[0] == 'Bob'
    assert table2[1].split(SEPARATOR)[1] == 'Nerd'
    assert re.match(r'\d+', table3[2].split(SEPARATOR)[2])
    assert table4[2].split(SEPARATOR)[3]