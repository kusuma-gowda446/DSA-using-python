class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = s.split()
        return " ".join(n[::-1])
       
