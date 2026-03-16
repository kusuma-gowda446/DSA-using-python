class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s=sorted(nums)
        n=len(nums)
        for i in range(n):
            r=s[i:]+s[:i]
            if r==nums:
                return True
        return False



        














       
