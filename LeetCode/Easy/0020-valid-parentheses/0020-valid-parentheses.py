class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        counter = 0
        while counter < len(s):
            if len(stack) == 0:
                stack.append(s[counter])
            else:
                match s[counter]:
                    case ")":
                        if stack.pop() != "(":
                            return False
                        else:
                            pass
                    case "]":
                        if stack.pop() != "[":
                            return False
                        else:
                            pass
                    case "}":
                        if stack.pop() != "{":
                            return False
                        else:
                            pass

                    case _:
                        stack.append(s[counter])


            counter += 1
        if len(stack) == 0:
            return True
        else:
            return False