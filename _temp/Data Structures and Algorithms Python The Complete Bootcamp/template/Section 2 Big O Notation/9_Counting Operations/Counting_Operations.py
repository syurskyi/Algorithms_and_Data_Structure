students _ ['andrew', 'akshat', 'chris', 'harshit', 'lary', 'tim', 'drake', 'ashish', 'shubham']


___ rondomFunction(students
    first _ students[0]  # O(1)
    total _ 0  # O(1)
    new_list _ []  # O(1)

    ___ student __ students:
        total +_ 1  # O(n)
        new_list.append(student)  # O(n)

    print(new_list)  # O(1)
    r_ total  # O(1)


print(rondomFunction(students))  # O(n) => O(n)