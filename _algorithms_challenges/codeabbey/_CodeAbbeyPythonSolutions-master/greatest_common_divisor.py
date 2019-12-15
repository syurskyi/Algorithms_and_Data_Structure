amount_values = int(input())
results = []

def gcd(num1, num2):
    if(num2 == 0):
        return num1
    else:
        num1, num2 = num2, (num1%num2)
        return(gcd(num1, num2))

def lcm(num1, num2):
    return num1*num2 // gcd(num1,num2)

def get_lcm_and_gcd(num1,num2):
    return "("+str(gcd(num1,num2))+" "+ str(lcm(num1, num2))+")"

for i in range(amount_values):
    num1, num2 = map(int, input().split())
    results.append(get_lcm_and_gcd(num1,num2))

print(*results)


