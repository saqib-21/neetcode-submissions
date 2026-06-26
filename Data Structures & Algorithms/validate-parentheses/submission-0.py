class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #maps the keys 
        closeToOpen = { ")" : "(", 
                        "]" : "[", 
                        "}" : "{" }

        for c in s:
            if c in closeToOpen: #if closing p, checks dictionary of closed keys
            #check if stack empty and then check top of stack (i= -1) to see if value (open p) of key c is in the stack
                if stack and stack[-1] == closeToOpen[c]: 
                    stack.pop()
                else:
                    return False
            else:
                #put first p in stack check
                print("in here now", c)
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False