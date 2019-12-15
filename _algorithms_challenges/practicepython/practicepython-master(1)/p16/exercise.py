import random, string

def generatePassword(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation + " "
    return ''.join(random.choice(alphabet) for i in range(length))

if __name__ == "__main__":
    random.seed()

    length = int(input("How long do you want the password to be? "))
    print(generatePassword(length))
