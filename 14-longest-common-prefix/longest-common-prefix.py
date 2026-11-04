class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = True
        prefix = ''
        shortest = min(strs, key=len)
        # take the first char of 1st word
        # check all(strs.startswith(prefix))
        # take next char 
        for x in range(0, len(shortest)):
            prefix += shortest[x]
            print(prefix)
            result = all(word.startswith(prefix) for word in strs)
            if result is False:
                prefix = prefix[:-1]
                break



        print(prefix)
        return prefix
