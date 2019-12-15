infile = open("prob127.txt")
infile.readline()
data = infile.readlines()
infile.close()

infile2 = open("prob127_dict.txt")
dictionary = infile2.readlines()
infile2.close()

##for word in data:
##    word = word.strip()
##    temp_d = [string.strip() for string in dictionary if len(string.strip())==len(word)]
##    count = 0
##    for each in temp_d:
##        flag = True
##        if each != word:
##            for char in word:
##                if word.count(char)!=each.count(char):
##                    flag = False
##                    break
##            if flag:
##                count+=1
##                
##    print(count,end=" ")


# ALT USING SORTED WORDS

for word in data:
    word = word.strip()
    word_s = sorted(list(word))
    temp_d = [string.strip() for string in dictionary if len(string.strip())==len(word)]
    count = 0
##    word_d = dict()
    for each in temp_d:
        flag = True
        if each != word:
            each = sorted(list(each))
            if each == word_s:
                count+=1
                
    print(count,end=" ")











    
