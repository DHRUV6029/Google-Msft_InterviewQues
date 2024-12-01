#  got a call from recruiter who submitted my profile for SWE did not discussed either it's E4 or E5 any such level.Just got interview lined up


# Q ) Try to write function for followin array [7,8,[3,4]] in such way that starting from index = 1 sum is calculated as


#   7*1+8*2+3*3+4*3 = 44
# Solution : Use recursion approach
# Verdict : Might be fail as I gave her backtracking kind of explaination even though interviewer told this can be resolved using recrusion approach.


arr  = [7,8,[3,4]]


class Solution:
    def __init__(self):
        self.total = 0
        self.d = 0

    def solve(self, arr):
        for i in range(0,len(arr)):
            #case-1 if its a int assiming there will only intergers
            if type(arr[i]) == int:
                self.d+=1
                self.total = self.total + (self.d) * arr[i]   
            elif type(arr[i]) == list:
                self.solve(arr[i])
                

        return self.total
    
s = Solution().solve(arr)   
print(s)
