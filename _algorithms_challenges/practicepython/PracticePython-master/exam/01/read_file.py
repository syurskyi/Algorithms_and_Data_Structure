try:
    fileObj = open("./file.dat","r", encoding="utf-8")

    for line in fileObj:
        print(line, end='')
        
    fileObj.close()
except Exception as e:
    print("無法開啟檔案", e)
