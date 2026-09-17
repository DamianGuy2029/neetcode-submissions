class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # creates a stack
        closeToOpen = { ")" : "(", "}" : "{", "]" : "[" } # Hashmap for closing parentheses
        # Maps closing to open parentheses
        for c in s: # for loop that iterates through s
            if c in closeToOpen: # if the value is found in hashmap...
                if stack and stack[-1] == closeToOpen[c]: # if stack is not empty
                    stack.pop() # and most recent stack addition is found in hashmap, then pop
                else: # else return False
                    return False
            else: # if value not in hashmap, that means it is open parentheses(add it to the stack)
                stack.append(c)
        return True if not stack else False # if the stack is empty then return True (otherwise it is False)