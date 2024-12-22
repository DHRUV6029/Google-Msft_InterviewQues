# Definition for a binary tree node.
import random
from typing import List , Optional
from collections import Counter, defaultdict , deque
import heapq

#########################################   
# Definition for a binary tree node.
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        bracket = {")":"(" , "}":"{" , "]":"["}
        #variation can contain all type of parenthesis 
        open = defaultdict(int)   #atmost conatins 3 values
        unclosed = defaultdict(int)
        to_delete_closed = defaultdict(int)

        for i in range(0,len(s)):
            if s[i] in '([{':
                #any open bracket is encountered
                open[s[i]]+=1
                unclosed[s[i]]+=1
            elif s[i] in ')]}':
                #this is a closfing bracket see if we have a unclosed corresponding bracket
                if unclosed[bracket[s[i]]]>0:
                    unclosed[bracket[s[i]]]-=1
                else:
                    #this needs to be deleted
                    to_delete_closed[s[i]]+=1

        allowed_open = {}
        for k, v in open.items():
            allowed_open[k] = v - unclosed[k]

        ans = ''
        #second pass to build the ans 
        for i in range(0,len(s)):
            if s[i]  in '([{':
                if allowed_open[s[i]]>0:
                    ans+=s[i]
                    allowed_open[s[i]]-=1
            elif s[i] in ')]}':
                if to_delete_closed[s[i]]>0:
                    to_delete_closed[s[i]]-=1
                else:
                    ans+=s[i]
            else:
                ans+=s[i]

        print(ans)

s =  Solution().minRemoveToMakeValid("(])[{")

        

                


        

            


