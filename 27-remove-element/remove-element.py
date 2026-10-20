class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] == val:
                k += 1
        
        nums[:] = [x for x in nums if x != val]
        