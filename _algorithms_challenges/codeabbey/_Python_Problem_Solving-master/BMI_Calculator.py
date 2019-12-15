def BMI_calculator():
    num_of_people =  int(input())
    result = []
    for i in range(0, num_of_people):
        weight,height = input().split()
        
        BMI = int(weight)/(float(height)**2)
        
        if BMI < 18.5:
            result.append('under')
        elif BMI >= 18.5 and BMI < 25.0:
            result.append('normal')
        elif BMI >= 25.0 and BMI < 30.0:
            result.append('over')
        elif BMI >= 30.0:
            result.append('obese')
        else:
            continue
    
    result = ' '.join(str(e) for e in result)
    print(result)
    
BMI_calculator()