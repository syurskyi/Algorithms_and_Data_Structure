def version_newer(old, new):
    o = [int(v) for v in old.split('.')]
    n = [int(v) for v in new.split('.')]
    if o[0] < n[0]:
        return True
    elif o[0] == n[0]:
        if o[1] < n[1]:
            return True
        elif o[1] == n[1]:
            if o[2] < n[2]:
                return True
    return False


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = [x.split('==') for x in (old_reqs.splitlines(keepends=False)) if len(x.strip()) > 0]
    new = [x.split('==') for x in (new_reqs.splitlines(keepends=False)) if len(x.strip()) > 0]
    for o, n in zip(old, new):
        if version_newer(o[1], n[1]):
            yield n[0]
