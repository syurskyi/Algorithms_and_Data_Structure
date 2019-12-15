class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        count = 0
        #i will track the length of the string
        i = 0
        while i != len(s):
            if s[i] == 'I':
                try:
                    if s[i+1]=='V':
                        count += 4
                        i += 2
                        continue
                    elif s[i+1]=='X':
                        count += 9
                        i += 2
                        continue
                except:
                    pass
            if s[i] == 'X':
                try:
                    if s[i+1]=='L':
                        count += 40
                        i += 2
                        continue
                    elif s[i+1]=='C':
                        count += 90
                        i += 2
                        continue
                except:
                    pass
            if s[i] == 'C':
                try:
                    if s[i+1]=='D':
                        count += 400
                        i += 2
                        continue
                    elif s[i+1]=='M':
                        count += 900
                        i += 2
                        continue
                except:
                    pass
            if s[i] in rom_dic:
                count += rom_dic[s[i]]
                i += 1
            
        return count
                