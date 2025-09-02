class Solution(object):
    def twoSum(self, nums, target):
        history = dict()
        for i in range(len(nums)):
            if target-nums[i] in history:
                return [history.get(target-nums[i])[0],i]
            pos=history.get(nums[i]) or list()
            pos.append(i)
            history[nums[i]] = pos