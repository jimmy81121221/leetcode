class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        
        count = 1
        left = 0
        for i in range(1, length):
            if nums[left] == nums[i]:
                continue
            else:
                nums[count] = nums[i]
                left = i
                count += 1
        return count
