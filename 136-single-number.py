from collections import Counter


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        return min(counts, key=counts.get)