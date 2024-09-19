class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        memo = {}

        def solve(start , end):
            #base case
            if (start , end) in memo:
                return memo[(start , end)]
            res = []
            if start == end:
                res.append(int(expression[start]))
                return res

            if end-start == 1 and expression[start].isdigit():
        
                res.append(int(expression[start:end+1]))
                return res

            for i in range(start , end+1):
                if expression[i].isdigit():
                    continue
        
                left = solve(start , i-1)
                right = solve(i+1 , end)

                for l in left:
                    for r in right:

                        #i will be always a operator as we are splitting on it
                        if expression[i] == "+":
                            res.append(int(l)+int(r))
                        elif expression[i] == '-':
                            res.append(int(l)-int(r))
                        elif expression[i] == '*':
                            res.append(int(l)*int(r))
            memo[(start , end)] = res
            return res

        ans = solve(0,len(expression)-1)
        return(ans)

        
