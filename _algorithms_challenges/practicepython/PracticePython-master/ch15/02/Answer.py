def div(x,y):
    try:
        return x / y
    except ZeroDivisionError as zde:
        print("除數不可為0!!")

user_input = input("將進行除法運算，請輸入兩個數字，並以逗點隔開:\n")

try:
    input_2_num = user_input.split(',')

    
    a = input_2_num[0].replace(' ','')
    b = input_2_num[1].replace(' ','')
    print(a, "/", b, "=", div(int(a),int(b)))

except (TypeError, ValueError) as teve:
    print("輸入資料型別或數值錯誤!!")
    
except IndexError as ie:
    print("輸入資料未以逗點','隔開!!")

finally:
    print("運算被執行")
