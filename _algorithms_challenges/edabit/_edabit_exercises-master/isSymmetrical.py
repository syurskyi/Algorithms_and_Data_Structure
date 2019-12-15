def is_symmetrical(num):
    if reversed(list(str(num))) == list(str(num)):
        return True
    else:
        return False


print(is_symmetrical(3223))
print(str(reversed(list(str(3223)))))
