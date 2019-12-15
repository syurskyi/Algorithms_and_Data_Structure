import random as r
import string
def PasswordGenerator():
    pwSize = 10
    chars = string.ascii_letters + string.digits + string.punctuation
    pw= ''.join(r.sample(chars,pwSize))
    print(pw)
    return pw