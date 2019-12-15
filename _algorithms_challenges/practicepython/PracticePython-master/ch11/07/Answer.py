a = [18, -51, 23, 35, 10, 9, -3, 52, 81, 69]
b = [28, 32, -35, 40, 73, 17, 92, 32, 13, 29]


def cross_multip(list1, list2):
    multip_sum = 0
    for i in range(len(list1)):
        multip_sum = multip_sum + a[i] * b[len(list2)-1 -i]

    return multip_sum

print(cross_multip(a, b))
