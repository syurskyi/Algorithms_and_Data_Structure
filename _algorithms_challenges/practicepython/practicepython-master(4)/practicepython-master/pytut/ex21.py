

#functions with return types

def add(a,b):
    print "this adds %r and %r and returns"%(a,b)
    return a+b


def sub(a,b):
    print "This subtracts %r and %r and returns"%(a,b)
    return a-b

def mul(a,b):
    print "This multiplies %r and %r and returns"%(a,b)
    return a*b

def div(a,b):
    print "This divides %r and %r and returns"%(a,b)
    return a/b


print "Lets do math with just functions"
age = add(30,5)
height = sub(78,4)
weight = mul(90,2)
iq = div(100,2)



print "Age: %r height: %r weight: %r iq: %r"%(age, height, weight, iq)
