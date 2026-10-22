class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        result = 0

        try:
            result = nums.index(target)
        except ValueError:
            if target < nums[0]:
                result = 0
            elif target > nums[len(nums) - 1]:
                result = len(nums)
            else:
                for i in range(1, len(nums)):
                    if nums[i - 1] < target and nums[i] > target:
                        result = i
                        break

        return result

        