class Solution:
    def maximumSwap(self, num: int) -> int:
        #TC - O(n)
        #SC - O(n)
        num = list(str(num))
        arr = [0]*len(num)
        arr[-1] = len(num)-1
        
        max_till_here_val = int(num[-1])
        max_till_here_idx = len(arr)-1
        idx1 , idx2 = -1 ,-1
        for i in range(len(num)-2, -1,-1):
            if int(num[i]) > max_till_here_val:  #we are recording the maxvalues till here
                max_till_here_val = int(num[i])
                max_till_here_idx = i

            elif int(num[i]) < max_till_here_val:
                #in this case this can be a candidiate for swap
                #its important to notive that it can be a candidate to swap do not swap here
                idx1 = i #smaller idx
                idx2 = max_till_here_idx

                #here we are recording the idx1, nd idx2 when we reach the left most part of the array 
                #idx2 will be the rightmost largest number and idx1 will be left msot larhest number
                
        if idx1 != -1 and idx2 != -1:
            num[idx1] , num[idx2] = num[idx2] , num[idx1]

        return int(''.join(num))
