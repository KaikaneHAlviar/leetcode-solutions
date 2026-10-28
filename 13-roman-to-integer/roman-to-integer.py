class Solution:

    def romanToInt(self, s: str) -> int:

        result = 0
        behind = 0

        convert = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }

        for index, char in enumerate(s):

            if index != 0:
                behind = convert[s[index - 1]]
            
            print(behind)
            # if the number "behind" index is ever less than number, subtract by x2 of less number
            if convert[char] > behind:
                result -= behind * 2

            result += convert[char]
        
        return result