class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))

        for val in range(len(x_list)):
            left = x_list[val]
            right = x_list[len(x_list) - 1 - val]
            if left != right:
                return False
        
        return True