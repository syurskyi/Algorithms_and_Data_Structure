''' Given a non-empty string like "Code" return a string like "CCoCodCode". '''


def string_splosion(str):
    new_str = ''
    if len(str) > 1:
        for i, _ in enumerate(str):
            new_str += str[:i + 1]
        return new_str
    return str
