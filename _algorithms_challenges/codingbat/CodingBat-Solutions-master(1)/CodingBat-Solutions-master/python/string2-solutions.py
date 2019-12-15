"""
  CodingBat String-2 Solutions

"""
"""

Given a string, return a string where for every char in the original, there are two chars. 

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
"""
def double_char(str):

    result = ""
    for i in range len(str):
        result = result + str[i]
        result = result + str[i]
        
    return result

"""
Return the number of times that the string "hi" appears anywhere in the given string. 

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""
def count_hi(str):

    for i in range (len(str)):
        if str[i] == 'h' and str[i+1] == 'i':
            counter+=1
    return counter

"""
Return True if the string "cat" and "dog" appear the same number of times in the given string. 

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""

def cat_dog(str):

    counter1 = 0
    counter2 = 0
    counter1 = str.count("cat")
    counter2 = str.count("dog")
    
    
    if(counter1 == counter2):
       return True
    else:
       return False

def cat_dog(str):
    return str.count("cat") == str.count("dog")


"""
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count. 

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""
def count_code(str):
    counter = 0
    for i in range (len(str)-3):
        if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
            counter += 1
    return counter
        
"""
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string. 

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""
def end_other(a, b):

    a1 = a.lower()
    b1 = b.lower()
 
    if a1.endswith(b1) or b1.endswith(a1):
        return True
    else:
        return False
    
"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not. 

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""
def xyz_there(str):

    return str.count('.xyz') != str.count('xyz')

    
