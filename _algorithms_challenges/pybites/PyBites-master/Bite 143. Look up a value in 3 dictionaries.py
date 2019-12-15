""" In this Bite you are presented with 3 dictionaries. 
Complete get_person_age that takes a name as argument and 
returns the age if in any of the 3 dictionaries. 
The lookup should be case insensitive, so tim, Tim and tiM
should all yield 30. If not in any of the dictionaries, return Not found.

Note that some persons are in 2 of the 3 dictionaries. 
In that case return the age of the last dictionaries 
(so group3 takes precedence over group2 and group2 takes precedence over group1). 
Check out the standard library ... :) - have fun! """

from collections import ChainMap

NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}

for i in group1, group2, group3:
    print(i['brenda'])

def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    name = str(name).lower()
    dict_set = ChainMap(group1, group2, group3)
    return dict_set.get(name, NOT_FOUND)



get_person_age(None)