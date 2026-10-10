class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for par in s:
            if len(stack) == 0:
                stack.append(par)
            else:
                match (par):
                    case ")":
                        if stack.pop() == "(":
                            continue
                        else:
                            return False
                    
                    case "]":
                        if stack.pop() == "[":
                            continue
                        else:
                            return False

                    case "}":
                        if stack.pop() == "{":
                            continue
                        else:
                            return False
                    
                    case _:
                        stack.append(par)

        if len(stack) == 0:
            return True
        else:
            return False
                    