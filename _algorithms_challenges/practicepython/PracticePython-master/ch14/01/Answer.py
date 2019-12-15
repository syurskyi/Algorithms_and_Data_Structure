with open("write.txt", "w+") as file:
    for i in range(5):
        hint = "請輸入"+ str(5-i)+ "次學生姓名及分數，請用空格隔開:\n"
        file.write(input(hint))
        file.write("\n")
