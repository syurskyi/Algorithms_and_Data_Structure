# Rule 5 - Remove all non-dominants

num_list = [1, 2, 3, 4, 5, 6, 7]


___ rondomFunction(num_list):
    total = 0  # O(1)
    all_integer = True  # O(1)

    ___ num __ num_list:
        print(num)  # O(n)

    ___ num1 __ num_list:
        ___ num2 __ num_list:
            print(num1, num2)  # O(n^2)
            total += 1  # O(n^2)

    msg = "Rule 5 - Remove all non-dominants"  # O(1)
    r_ total  # O(1)


print(rondomFunction(num_list))  # O(n^2)