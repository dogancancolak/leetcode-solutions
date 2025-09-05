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
        key = -101
        unique_pos = 0
        while unique_pos < len(nums):
            idx = unique_pos
            while key >= nums[idx]:
                idx +=1
                if idx == len(nums):
                    return unique_pos
            nums[unique_pos]= nums[idx]
            key = nums[unique_pos]
            unique_pos +=1
    
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
