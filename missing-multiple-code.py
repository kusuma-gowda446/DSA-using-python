class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=set(nums)
        m=k
        while m in nums:
            m+=k
        return m 
