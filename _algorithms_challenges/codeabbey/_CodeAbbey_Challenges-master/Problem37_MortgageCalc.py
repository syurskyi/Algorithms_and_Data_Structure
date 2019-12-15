infile = open("prob37.txt")
data = infile.read()
infile.close()

s,r,t = [int(i) for i in data.strip().split(" ")]
r = r/12
m = (s*(r/100)*(1+r/100)**t)/((1+r/100)**t-1)

print(round(m))
