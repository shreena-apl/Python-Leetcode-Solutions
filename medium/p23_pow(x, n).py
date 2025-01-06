# Pow(x, n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        #i=0
        value=float('inf')
        if n == 0:
            return 1
        value = x**n
        return value