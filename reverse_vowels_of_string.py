class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n="aeiouAEIOU"
        v=[]
        for ch in s:
            if ch in n:
                v.append(ch)
        result=""
        for ch in s:
            if ch in n:
                result+=v.pop()
            else:
                result+=ch
        return result
        


        
