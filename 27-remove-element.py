class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        pop_positions = []
        for i in range(len(nums)):
            if nums[i] == val:
                pop_positions.append(i)
        for idx in reversed(pop_positions):
            nums.pop(idx)
        return len(nums)