#Here we calculate the input n like n+nn+nnn - say input is 5: 5+55+555 = 615
cal = input("Write a number here to calculate n+nn+nnn : ")
n1 = int( "%s" % cal)
n2 = int( "%s%s" % (cal,cal))
n3 = int( "%s%s%s" % (cal,cal,cal))
print(n1+n2+n3)