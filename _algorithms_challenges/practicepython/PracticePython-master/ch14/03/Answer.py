

with open("./data.txt", "a+") as data:
    for i in range(5):
        hint = "請輸入"+ str(5-i) + "個人的姓名: "
        data.write(input(hint)+"\n")
