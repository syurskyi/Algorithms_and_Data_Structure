## 因為要輸入一串數值串列，所以我搜尋python input list
input_string = input("請輸入一串數值串列(以','隔開數值):\n")


#input_list = list(input_string.split(','))
#input_list = list(map(int, input_list))
## 搜尋python list to int
## 使用map方法把list的字串型態轉為int型態
input_list = list(map(int, input_string.split(',')))



def biggest(num_list):
    print("最大值",max(num_list))
    print("最小值",min(num_list))

biggest(input_list)

