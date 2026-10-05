class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = []
        for ch in s:
            if ch.isalnum():
                char.append(ch.lower())
            
        if char == char[::-1]:
            return True
    
            
        
        return False
       