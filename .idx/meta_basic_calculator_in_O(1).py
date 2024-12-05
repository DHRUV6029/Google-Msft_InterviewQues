#################################################
from typing import List, Optional
import heapq, bisect, collections
#################################################

class Solution:
    def calculate(self, s: str) -> int:

        #Approch need to track 3 things at any point i 
        #last_number, cur_number , last_ops   
        #at any point i if we check and process the last exp
        res = 0
        last_num = 0
        last_op = "+"
        cur_num = 0

        for i in range(0 ,len(s)):
            if s[i].isdigit():
                cur_num = cur_num*10 + int(s[i])
            if (not s[i].isdigit()) and (s[i] != ' ') or (i == len(s)-1):
                
                if last_op == "+" or last_op == '-':
                    res+=(last_num)

                    last_num = cur_num if last_op == "+" else - cur_num

                elif last_op == "*":
                    last_num = last_num * cur_num
                elif  last_op == '/':
                    last_num = int(last_num / cur_num)

                
                last_op = s[i]
                cur_num = 0

        res+=last_num

        return res
    


#Dry run
# res = 3
# last_num,cur_num,last_op
# 0          0        +    Inint
# 0          3        +    i = 0
# 3          0        +    i = 1
# 3          5        +    i = 2
# 5          0        /    i = 3
# 2          2        2    i = 4

# 3+2 = 5



s = Solution().calculate(s = " 3/2 ")
print(s)



            

            



