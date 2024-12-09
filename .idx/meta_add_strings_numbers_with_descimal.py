#################################################
from typing import List, Optional
import heapq, bisect, collections, random
#################################################
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        num1 = num1.split('.')
        num2 = num2.split('.')

        left1 , left2 = num1[0] , num2[0]
        right1 , right2 = num1[1] if len(num1)>1 else '' ,  num2[1] if len(num2)>1 else ''

        carry = 0

        #process the deicmal part first
        r1 , r2  = len(right1)-1 , len(right2)-1
        
        ans= ''

        while r1 != r2:
            if r1 > r2:
                ans+=right1[r1]
                r1-=1
            elif r2 > r1:
                r2-=1
                ans+=right2[r2]
                

        while r1 >= 0 and r2 >= 0:
            val = (int(right1[r1]) + int(right2[r2]) + carry)%10
            carry = (int(right1[r1]) + int(right2[r2]) + carry) //10
            ans+=(str(val))
            r1-=1
            r2-=1


        ans+='.'


        #processs the left part
        l1, l2 = len(left1)-1 , len(left2)-1

        while l1 >= 0 or l2 >= 0:
            v1 = int(left1[l1]) if l1 >= 0 else 0
            v2 = int(left2[l2]) if l2 >= 0 else 0

            val = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) //10

            ans+=(str(val))

            l1-=1
            l2-=1

        if carry!=0:
            ans+=str(carry)

        ans = ans[::-1]
        return ans if ans[-1] != '.' else ans[: len(ans)-1]

s = Solution().addStrings(num1 = "152.9981", num2 = "122.9")
print(s)
        
