
while(1):
    try:
        path = input("請輸入欲開啟的檔案名稱:\n")
        with open(path, "r+") as fileObj:
            lines = fileObj.readlines()
            for line in lines:
                print(line)
            break

    except:
        print("檔案不存在!!",end= '')
