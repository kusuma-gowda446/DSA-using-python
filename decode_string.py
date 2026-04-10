class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        curr=""
        stack=[]
        num=0
        for c in s:
            if c.isdigit():
                num=num*10+int(c)

            elif c=="[":
                stack.append((curr,num))
                curr=""
                num=0
            elif c=="]":
                prev_str,count=stack.pop()
                curr=prev_str+curr*count
            else:
                curr+=c
        return curr



        
