class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        drum1=[]
        drum2=[]
        for i in s:
            if i=="#":
                if drum1:
                    drum1.pop()
            else:
                drum1.append(i)
        for j in t:
            if j=="#":
                if drum2:
                    drum2.pop()
            else:
                drum2.append(j)
        return drum1==drum2

                
        
