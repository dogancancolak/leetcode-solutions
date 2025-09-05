class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     key = None
    #     max_lentgth = len(nums)
    #     idx = 0
    #     while idx < max_lentgth:
    #         if idx == max_lentgth:
    #             break
    #         if nums[idx] == key:
    #             nums.pop(idx)
    #             max_lentgth -=1
    #         else:
    #             key = nums[idx]
    #             idx += 1
    #     return len(nums)

    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     key = None
    #     tb_remove = []
    #     for num in nums:
    #         if num == key:
    #             tb_remove.append(num)
    #         else:
    #             key = num
    #     for elem in tb_remove:
    #         nums.remove(elem)
    #     return len(nums)

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        write = 1
        for read in range(1, len(nums)): 
            if nums[read] != nums[read - 1]: 
                nums[write] = nums[read] 
                write += 1 

        return write
