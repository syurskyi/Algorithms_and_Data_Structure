
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open("./PPAP.txt", "r+") as fileObj:
    text = str(fileObj.readlines())
    
    ## 搜尋 python count char in string
    for i in alphabet:
        print(i, " : ",text.count(i))

    ## 因為敘述只有提到小寫字母，
    ## 若要將大寫字母也加進來，則搜尋python to lower case (將大寫字母轉為小寫
    #print(text.lower())
    #for i in alphabet:
    #    print(i, " : ",text.lower().count(i))    
