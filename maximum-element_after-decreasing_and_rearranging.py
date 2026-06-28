class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()

        ans = 1 
        for i in range(1, len(arr)):
            ans = min(arr[i], ans + 1)

        return ans
        
