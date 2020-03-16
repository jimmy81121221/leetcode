class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic_nums = {}
        len_nums = len(nums)
        for i in range(len_nums):
            if target - nums[i] in dic_nums:
                return [dic_nums[target - nums[i]], i]
            else:
                dic_nums[nums[i]] = i
