class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars=sorted(zip(position,speed),reverse=True)
        fleet=0
        prev=0
        for pos,spd in cars:
            time = float(target - pos) / spd
    
            if time>prev:
                fleet+=1
                prev=time

        return fleet
        
