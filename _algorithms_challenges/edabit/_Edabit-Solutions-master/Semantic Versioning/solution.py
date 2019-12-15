def retrieve_major(semver):
    a = semver.split(".")
    return a[0]



def retrieve_minor(semver):
    a = semver.split(".")
    return a[1]


def retrieve_patch(semver):
    a = semver.split(".")
    return a[2]
