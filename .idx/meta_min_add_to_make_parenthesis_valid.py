class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        ans = 0
        for i in range(0,len(s)):
            if s[i] == '(':
                balance+=1

            else:
                if balance>0:
                    balance-=1
                else:
                    ans+=1

        return ans + balance
