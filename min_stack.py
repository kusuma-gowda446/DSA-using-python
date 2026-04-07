class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if (len(self.minstack)==0)or val<=self.minstack[-1]:
            self.minstack.append(val)


        

        

    def pop(self):
        """
        :rtype: None
        """
        if (len(self.stack)==0):
            return"empty stack"
        else:
            top=self.stack.pop()
        if top==self.minstack[-1]:
            return self.minstack.pop()
        else:
            return"stack is empty"
        

    def top(self):
        """
        :rtype: int
        """
        if(len(self.stack)==0):
            return"stack is empty"
        else:
            return self.stack[-1]

        

    def getMin(self):
        """
        :rtype: int
        """
        if (len(self.minstack)==0):
            return"empty min stack"
        else:
            return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
