def say_hello_bye(name, num):
    if num == 1:
        return "Hello " + name.capitalize()
    else:
        return "Bye " + name.capitalize()


def test():
    print("test has started")
    if say_hello_bye("ram", 2) != "Bye Ram":
        print("error1")
    if say_hello_bye("jodu", 1) != "Hello Jodu":
        print("error2")
