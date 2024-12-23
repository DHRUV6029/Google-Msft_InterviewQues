# Given an integer array and limit number. Print numbers in a 
# certain level of lines where a comma separates numbers 
# and each line length must fit in the limit.
# In addition, each line must finish with a comma except 
# for the last line. The comma is counted in the line length


arr = [1, 23, 5, 234, 5, 563, 123 ]
limit=5

#Assumption You cannot break the number so len(nums[i]) <= limit-1 , so its guareented that a 
#single 
ans = []
def print_in_line(arr):
    i = 0
    limit = 5
    cur_line = ''
    cur_limit = limit

    while i < len(arr):
        cur_limit-=(len(str(arr[i]))+1)
        if cur_limit >= 0:
            cur_line+=str(arr[i])+','
        else:
            ans.append(cur_line)
            cur_line = str(arr[i])+','
            cur_limit = (limit - len(cur_line))
        
        i+=1
    
    ans.append(cur_line)
    
    return ans

    
s =print_in_line(arr)
print(s)

