class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        removed = 0
        x = 0

        while x < len(nums):
            
            if x + 1 < len(nums) and nums[x] == nums[x + 1] and nums[x] != 101:
                del nums[x + 1]
            else:
                x += 1

        
        return len(nums) - removed

 # compare last seen non-duplicate
 # k = len(nums) - shift (the number of values we've deleted)
 # python.sort()
 # replace shifted numbers with 101 instead of empty space