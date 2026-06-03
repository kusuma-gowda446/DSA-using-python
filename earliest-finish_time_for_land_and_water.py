class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
     
        
       
        minA = min(s + d for s, d in zip(landStartTime, landDuration))

        
        ans1 = float('inf')
        for ws, wd in zip(waterStartTime, waterDuration):
            ans1 = min(ans1, wd + max(ws, minA))

        
        minB = min(s + d for s, d in zip(waterStartTime, waterDuration))

        
        ans2 = float('inf')
        for ls, ld in zip(landStartTime, landDuration):
            ans2 = min(ans2, ld + max(ls, minB))

        return min(ans1, ans2)
        
