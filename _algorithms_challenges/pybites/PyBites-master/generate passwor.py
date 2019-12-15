import string
import secrets

aplphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(aplphabet) for i in range(10))


