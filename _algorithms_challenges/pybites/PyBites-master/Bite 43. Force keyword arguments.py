"""Write a function called get_profile that can only allows 2 keyword arguments: name and profession which default to julian and programmer respectively.

The function does nothing fancy, just return a str: name is a profession.

The point is to limit the interface of this function and you'll see Python makes it very easy ... have fun!"""


def get_profile(*,name='julian', profession='programmer'):
        return f'{name} is a {profession}'