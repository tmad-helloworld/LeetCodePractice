class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[0::1] == x[::-1]:
            return True

        return False
        
            
            