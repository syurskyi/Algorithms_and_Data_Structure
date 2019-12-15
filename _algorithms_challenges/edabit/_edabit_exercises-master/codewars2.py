# return masked string
def maskify(cc):
    return '#' * (len(cc) - 4) + cc[-4:]


print(maskify('4556364607935616'))
