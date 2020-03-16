class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        length = len(nums)
        i = 0
        for i in range(length - 2):
            if(nums[i] != nums[i-1] or i == 0):
                target = 0 - nums[i]
                left = i + 1
                right = length - 1
                while left != right:
                    if nums[left] + nums[right] == target:
                        ans.append([nums[i], nums[left], nums[right]])
                        while left < right:
                            left += 1
                            if(nums[left] != nums[left-1]):
                                break
                        while left > right:
                            right -= 1
                            if(nums[right] != nums[right+1]):
                                break
                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
        return ans