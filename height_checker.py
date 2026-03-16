class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s=sorted(heights)
        n=len(heights)
        c=0
        for i in range(n):
            if (heights[i]!=s[i]):
                c+=1
        return c


        
