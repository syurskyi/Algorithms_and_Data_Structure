import re


def strip_comments(code):
    # strip docstrings first
    cd = re.sub(r'\s*"""[\w\W]*?"""\s*?\n', r'\n', code)
    # turn into a list
    cd = [line.rstrip() for line in cd.splitlines(keepends=False)]
    # chop out in line comments
    cd = [re.sub(r' {2}# .*', '', line) for line in cd if len(line) < 1 or not re.match(r'^\s*#', line)]
    return '\n'.join(cd)
