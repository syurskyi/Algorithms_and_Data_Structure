with open("prob15.txt") as infile:
    min_ = 0
    max_ = 0
    data = infile.read()
    data = data.split(" ")
    for each_digit in data:
        each_digit =int(each_digit)
        if int(each_digit) < min_:
            min_ = each_digit
        if int(each_digit) > max_:
            max_ = each_digit

    print(max_,min_)
    
