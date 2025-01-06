# Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x < 0:
            sign = -1
        else:
            sign = 1
        x*=sign
        for i in str(x):
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10
        if rev < -2**31 or rev > (2**31)-1:
            return 0
        else:
            return rev*sign