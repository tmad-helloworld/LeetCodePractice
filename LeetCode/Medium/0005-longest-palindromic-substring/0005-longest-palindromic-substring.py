

class Solution:
    def expandFromMiddle(self,left,right,s):
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]
            
                
    
    def longestPalindrome(self, s: str) -> str:
        subString = ""
        
        for i in range(0,len(s)):
            odd = self.expandFromMiddle(i,i,s)
            if len(odd) > len(subString):
                subString = odd

            
            even = self.expandFromMiddle(i,i+1,s)
            if len(even) > len(subString):
                subString = even

        
        return subString
            
           
                
            
            
        

                
                
            
            