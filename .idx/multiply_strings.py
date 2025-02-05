class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return 0
        
        ans = [0]*(len(num2) + len(num1))
        num1 = num1[::-1]
        num2 = num2[::-1]
    
        for i in range(0,len(num1)):
            for j in range(0 ,len(num2)):
                offset = i+j
                c = ans[offset]
                tmp = (int(num1[i]) * int(num2[j]) + c)%10
                ans[offset] = tmp
                c = (int(num1[i]) * int(num2[j]) + c)//10
                ans[offset+1]+=c
            
        if ans[-1] == 0:
            ans.pop()

        return ''.join(str(i) for i in ans[::-1])



    
s = Solution().multiply('2','3')
print(s)
