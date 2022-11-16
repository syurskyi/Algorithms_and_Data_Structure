c_ Solution:
    ___ findHashs
        r_ ''.join(sorted(s))
    ___ groupAnagrams strs: List[str]) -> List[List[str]]:
        answers _ []
        m _ {}

        ___ s __ strs:
            hashed _ findHash(s)
            __(hashed n.. __ m
                m[hashed] _ []
            m[hashed].append(s)
        
        ___ p __ m.values(
            answers.append(p)
        
        r_ answers

