class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for i,n  in enumerate(nums):
            count=target-n
            if count in seen:
                return [seen[count],i]
            seen[n]=i


              




        
