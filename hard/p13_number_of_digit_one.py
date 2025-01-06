# Number of Digit One

class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0

        pow10 = 1
        while pow10 <= n:
            divisor = pow10 * 10
            quotient = n // divisor
            remainder = n % divisor
            if quotient > 0:
                ans += quotient * pow10
            if remainder >= pow10:
                ans += min(remainder - pow10 + 1, pow10)
            pow10 *= 10

        return ans
        # res=0
        # if n==0:
        #     return 0
        # for i in range(1,n+1):
        #     while(i>=1):
        #         digit=i%10
        #         if digit == 1:
        #             res+=1
        #         i=i//10
        #         if i==0:
        #             continue
        # return res
        