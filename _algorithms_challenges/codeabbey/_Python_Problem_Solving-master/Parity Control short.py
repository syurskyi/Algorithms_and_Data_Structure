answers = []
for i in input().split():
    c = bin(int(i))
    if not c.count("1") % 2:
        answers.append(chr(int(i) % 128))

print(''.join(answers))