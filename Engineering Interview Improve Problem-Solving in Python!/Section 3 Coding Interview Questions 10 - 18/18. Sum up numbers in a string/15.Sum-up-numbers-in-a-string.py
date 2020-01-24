# "asddas22asda3fdf4aaaaa444" => 22  3 + 4 = 29

def count_number(s):
    temp = 0
    total = 0
    for c in s:
        if '0' <= c and c <= '9': # only <<<<<<<<<<<<<
            temp *= 10
            temp += int(c)
        else:
            total += temp
            temp = 0
    total += temp
    return total

print(count_number("asddas22asda3fdf4"))