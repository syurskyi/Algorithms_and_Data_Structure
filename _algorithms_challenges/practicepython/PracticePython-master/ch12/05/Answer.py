class CTime():

    def __init__(self):
        self.__hour = '00'
        self.__minute = '00'
        self.__second = '00'

    def set_value(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def GetTime(self):
        return self.__hour, self.__minute, self.__second


input_h = input("欲設定時間，\n請輸入小時:\n")
input_m = input("請輸入分:\n")
input_s = input("請輸入秒:\n")
print()

hms = CTime()
hms.set_value(input_h, input_m, input_s)
time = hms.GetTime()

for i in range(len(time)):
    if i == len(time)-1:
        print(time[i])
    else:
        print(time[i], end=':')
