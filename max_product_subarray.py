ef maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product=min_product=result=nums[0]
        for i in range (1,len(nums)):
            curr=(nums[i],max_product*nums[i],min_product*nums[i])
            max_product=max(curr)
            min_product=min(curr)
            result=max(max_product,result)
        return result
