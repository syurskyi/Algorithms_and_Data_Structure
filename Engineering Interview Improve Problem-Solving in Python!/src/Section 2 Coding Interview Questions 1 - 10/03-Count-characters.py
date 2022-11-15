# aabsbddb ... a = 2, b = 3, s = 1, d = 2

def count_characters(s):
    result = {}
    for c in s:
        result[c] = result.get(c, 0) + 1
    for key, value in result.items():
        print(key, value)
    #return result

count_characters('aabsbddb')