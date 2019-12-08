numbers = [10, 20, 300, 40.5, 50];

# random indexing --> O(1) get items if we know the index !!!
# print(numbers[4]);

# numbers[1] = 'Adam';

# print(numbers[1]);

# for num in numbers:
#	print(num);


# for i in range(len(numbers)):
#	print(numbers[i]);

# print(numbers[:-2]);

# O(N) search running time   
maximum = numbers[0];
for num in numbers:
    if num > maximum:
        maximum = num;

print(maximum);
