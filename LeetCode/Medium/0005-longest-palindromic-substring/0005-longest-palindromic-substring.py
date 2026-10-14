class Solution:
    def expandFromMiddle(self, left, right, s):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        counter = 0
        longest = ""
        for ch in s:
            odd = self.expandFromMiddle(counter, counter, s)
            longest = max(odd, longest,key=len)

            even = self.expandFromMiddle(counter, counter + 1, s)
            longest = max(even, longest,key=len)

            counter += 1
            

        return longest
