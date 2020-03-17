class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ans = 0
        isPlus = 1
        if x < 0:
            isPlus = -1
            x = isPlus * x
            
        while x != 0:
            ans = ans * 10 + x % 10
            x /= 10
            if ans > 2 ** 31 - 1:
                return 0
            
        return ans * isPlus
