c_ Solution:

    ___ backtracking ans, m, digits, combination, index
        __(index > len(digits)):
            r_
        __(len(combination) == len(digits)):
            ans.append(combination[:])
            r_

        currentDigit _ digits[index]
        curString _ m[currentDigit]

        ___ i __ range(len(curString)):
            backtracking(ans, m, digits, combination +
                              curString[i], index+1)

    ___ letterCombinations digits: str) -> List[str]:
        ans _ []
        __(len(digits) == 0
            r_ ans

        m _ {}

        m['2'] _ "abc"
        m['3'] _ "def"
        m['4'] _ "ghi"
        m['5'] _ "jkl"
        m['6'] _ "mno"
        m['7'] _ "pqrs"
        m['8'] _ "tuv"
        m['9'] _ "wxyz"

        backtracking(ans, m, digits, "", 0)

        r_ ans
