class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        ans = []
        N = len(num)
        def helper(idx , prev , cur , res , path):
            #base case
            if idx == N:
                if res == target and cur == 0:
                    ans.append(''.join(str(x) for x in path[1:]))
                return 

            
            cur = cur * 10 + int(num[idx])
            str_cur = int(cur)

            if cur > 0:
                helper(idx+1 , prev , cur , res, path)

            #Additions
            path.append("+") , path.append(str_cur)
            helper(idx+1 , cur , 0 , res+cur , path)
            path.pop() , path.pop()

            if path:
                #do not add -1 to empty val 

                #Subtraction
                path.append("-") , path.append(str_cur)
                helper(idx+1 , -cur , 0 , res-cur , path)
                path.pop() , path.pop()

                #Multiplication its little bit complicated 
                path.append("*") , path.append(str_cur)
                #Eg 103*6
                # 13 * 6 = 78  this is incorrect
                # 10+18 = 38 this is correct 

                # prev = 3
                # Value = 13  How to get the value 13 - 3 = 10 + 3*6
                # formula value - prev + (cur * prev)
                helper(idx+1 , cur*prev , 0 , res - prev + (cur * prev) ,path)
                path.pop() , path.pop()

        helper(0,0,0,0,[])
        return ans


s = Solution().addOperators('123' , 6)
print(s)
