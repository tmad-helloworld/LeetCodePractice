class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for par in s:
            match (par):
                case ")":
                    if len(stack) > 0:
                        if stack.pop() == "(":
                            continue
                        else:
                            return False
                    else:
                        return False
                    
                case "]":
                    if len(stack) > 0:
                        if stack.pop() == "[":
                            continue
                    
                        else: 
                            return False
                    else:
                        return False

                case "}":
                    if len(stack) > 0:
                        if stack.pop() == "{":
                            continue

                        else:
                            return False
                    else:
                        return False
                        
                case _:
                    stack.append(par)
                    continue

        if len(stack) == 0:
            return True
        else:
            return False
                    