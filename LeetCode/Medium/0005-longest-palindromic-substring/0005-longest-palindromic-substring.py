

class Solution:
    def expandFromMiddle(self,s:str, left: int, right: int) -> str:
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1


        return s[left + 1:right]
    
    def longestPalindrome(self, s: str) -> str:
        substring = ""
        for i in range(0,len(s)):
            odd = self.expandFromMiddle(s,i,i)
            if len(odd) > len(substring):
                substring = odd

            even = self.expandFromMiddle(s,i,i+1)
            if len(even) > len(substring):
                substring = even

        return substring


                
                
            
            