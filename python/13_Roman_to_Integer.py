class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        last = 0
        ans = 0
        for i in s:
            ans += roman[i]
            
            if roman[i] > last:
                ans -= 2 * last
                
            last = roman[i]
            
        return ans
