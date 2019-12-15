class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        tab = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        store_trans = []
        for i in words:
            string = ''
            for j in i:
                ind = ord(j) - 97
                string += tab[ind]
            if string not in store_trans:
                store_trans.append(string)
        return len(store_trans)