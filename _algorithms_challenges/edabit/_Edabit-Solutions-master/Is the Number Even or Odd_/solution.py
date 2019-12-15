def isEvenOrOdd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"


def test():
    print("test has started")
    if isEvenOrOdd(3) != "odd":
        print("error1")
    if isEvenOrOdd(0) != "even":
        print("error2")
    if isEvenOrOdd(-3) != "odd":
        print("error3")
    if isEvenOrOdd(-0) != "even":
        print("error4")
