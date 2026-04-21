class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))   # remove duplicates + sort
        
        if len(nums) < 3:
            return nums[-1]        # return max
        else:
            return nums[-3]        # return 3rd max
