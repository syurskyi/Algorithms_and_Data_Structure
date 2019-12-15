"""In this bite you will work with a list of names.

First you will write a function to take out duplicates and title case them.

Then you will sort the list in alphabetical descending order by surname and lastly determine what the shortest first name is. For this exercise you can assume there is always one name and one surname.

With some handy Python builtins you can write this in a pretty concise way. Get it sorted :)"""

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    names = list(set(NAMES))
    func_names = []
    for i in names:
        i = i.title()
        func_names.append(i)
    return func_names


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(NAMES)
    name_dict = []
    for i in names:
        i = i.split()
        name_dict.append({'name':i[0], 'surname': i[1]})
    sort_names = list(sorted(name_dict, key=lambda k: k['surname'], reverse=True))
    names = []
    for a in sort_names:
        s = str(a['name']) + ' ' + str(a['surname'])
        names.append(s)
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    name_dict = []
    for i in names:
        i = i.split()
        name_dict.append({'name':i[0], 'surname': i[1]})
    short_name_sort = sorted(name_dict, key=lambda k: len(k['name']))
    return short_name_sort[0]['name']