class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)
        count = 0
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] == t[i]:
                count += 1
        if count == len(t):
            return True
        else:
            return False
        
