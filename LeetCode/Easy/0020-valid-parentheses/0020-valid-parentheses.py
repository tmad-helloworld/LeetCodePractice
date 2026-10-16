class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if len(stack) == 0:
                stack.append(ch)
            else:
                match (ch):
                    
                    case ")":
                        if stack.pop() == "(":
                            continue
                        else:
                            return False
                    
                    
                    case "}":
                        if stack.pop() == "{":
                            continue
                        else:
                            return False
                    
                    case "]":
                        if stack.pop() == "[":
                            continue
                        else:
                            return False
                    case _:
                        stack.append(ch)

        if len(stack) != 0:
            return False 
        return True