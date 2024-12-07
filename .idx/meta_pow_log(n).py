
class Solution:
    def myPow(self, x: float, n: int) -> float:
        is_neg = True if n < 0 else False

        n = abs(n)
        ans = 1

        if n== 0:return 1


        while n > 1:
            if n%2==1:
                ans*=x

            x = x * x
            n//=2

        ans = ans * x

        if is_neg:
            return (1/ans)

        return ans
