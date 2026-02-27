def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur=maxi=nums[0]
        for i in range(1,len(nums)):
            cur=max(nums[i],cur+nums[i])
            maxi=max(cur,maxi)
        return maxi
        
