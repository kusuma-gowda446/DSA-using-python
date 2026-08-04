class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums=set(nums) #because it doesnot allow duplication
        start=min(nums)  # since we need to find the missing number between smallest and largest given numbers this takes the samllest number in the list 
        end=max(nums)  # this takes the largest number in the list 
        n=[] #declare a empty set to assign the missing value 
        for i in range (start,end+1): #now run the loop from smallest element to the largest element 
            if i not in nums: # if the element in the nums is not in the set 
                n.append(i)  # append it to n 

        return n   #return n coz it carries the missing number 


        
