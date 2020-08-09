"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The solution is based on two-finger swapping.
"""
class Solution:
    def removeDuplicates(self, nums):
        nums_len = len(nums)

        if(nums_len < 0):
            return 0

        current_indx = 0
        while current_indx < len(nums) - 1:
            if(nums[current_indx] == nums[current_indx + 1]):
                del nums[current_indx + 1]
            else:
                current_indx += 1

        return len(nums)
