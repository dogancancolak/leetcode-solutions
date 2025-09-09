class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = dict()
        for num in nums:
            frequency[num] = frequency.get(num,0) +1
            if frequency[num] > len(nums)/2:
                return num