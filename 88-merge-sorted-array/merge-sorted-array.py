class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        count_back = 0 - len(nums2)
        while count_back < 0:
            nums1[count_back] = nums2[count_back]
            count_back += 1
        
        nums1.sort()


        