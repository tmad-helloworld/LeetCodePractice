class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        backward = ""
        for i in range(0,len(s)):
            if s[i].isalnum():
                forward = forward + s[i]
            if s[-1-i].isalnum():
                backward = backward + s[-1-i]

            
        if forward.lower() == backward.lower():
            return True
        
        else:
            return False
        