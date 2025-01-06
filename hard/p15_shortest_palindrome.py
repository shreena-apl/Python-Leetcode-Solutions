# Shortest Palindrome

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s.strip())==0:
            return s

        t = s[::-1]

        for i in range(len(t)):
            if s.startswith(t[i:]):
                return t[:i] + s

        