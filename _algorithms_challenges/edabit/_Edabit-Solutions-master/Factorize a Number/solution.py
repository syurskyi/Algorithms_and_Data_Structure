def factorize(num):
    index = 1
    output = []
    while index <= num:
        if num % index == 0:
            output.append(index)
        index = index + 1
    return output
	
