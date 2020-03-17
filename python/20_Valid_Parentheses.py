class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length == 0:
            return True
        
        if length % 2 != 0:
            return False
        
        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False
        
        stack = []
        
        for i in s:
            if i == ')':
                current = stack.pop()
                if current != '(':
                    return False
            elif i == ']':
                current = stack.pop()
                if current != '[':
                    return False
            elif i == '}':
                current = stack.pop()
                if current != '{':
                    return False
            else:
                stack.append(i)
                
        if stack == []:
            return True
        else:
            return False
