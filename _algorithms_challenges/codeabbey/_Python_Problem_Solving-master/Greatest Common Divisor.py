a =  int(input())
string = ''
for i in range(a):
    temp1,temp2 = num1, num2 = [int(ele) for ele in input().split()]
    while num1 !=  num2:   
        if num1 >  num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1  
    lcm = temp1 * temp2 / num1
    string += '('+str(num1)+' '+str(int(lcm))+')'
    string += ' '  
print(string)