primenumbers = set()
happynumbers = set()

with open('primenumbers.txt', 'r') as primes:
    line = primes.readline()
    while line:
        primenumbers.add(int(line))
        line = primes.readline()

with open('happynumbers.txt', 'r') as happys:
    line = happys.readline()
    while line:
        happynumbers.add(int(line))
        line = happys.readline()

#print(primenumbers)
#print(happynumbers)

overlap = primenumbers.intersection(happynumbers)
print(overlap)
