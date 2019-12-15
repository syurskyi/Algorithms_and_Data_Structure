def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    names = [name.split()[0] for name in names]
    return min(names, key=len)