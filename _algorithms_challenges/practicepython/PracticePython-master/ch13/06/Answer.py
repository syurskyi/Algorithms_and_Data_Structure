import random

record_list = [0 for i in range(10)]
print(record_list)

for i in range(1000):
    rand_int = random.randint(1, 100)
    
    if rand_int <= 10:
        record_list[0] = record_list[0] + 1
    elif rand_int <= 20:
        record_list[1] = record_list[1] + 1
    elif rand_int <= 30:
        record_list[2] = record_list[2] + 1
    elif rand_int <= 40:
        record_list[3] = record_list[3] + 1
    elif rand_int <= 50:
        record_list[4] = record_list[4] + 1
    elif rand_int <= 60:
        record_list[5] = record_list[5] + 1
    elif rand_int <= 70:
        record_list[6] = record_list[6] + 1
    elif rand_int <= 80:
        record_list[7] = record_list[7] + 1
    elif rand_int <= 90:
        record_list[8] = record_list[8] + 1
    elif rand_int <= 100:
        record_list[9] = record_list[9] + 1

for i in record_list:
    print(i)
