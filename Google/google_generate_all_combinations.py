# I received following question I solved using recusrion , interviewer was concerned can it more optimized
# Musical scales are represented by the these threee number 1,2,3 ,you need to generate all the possible combination of musical scale which sum to 12 and the consecutive pattern should be followed .
# 1>2,3
# 2>-1,2
# 3>1
# The above states that after 1 only musical scale 2, 3 could come not 1 ,similary after 2 , 1 and 2 can come not 3 and after 3 ,1 can come .
# Also the start and end of the pattern should be consecutive as well .Example
# 1,2,2,3,1,2,1 -> is not valid because the last scale 1 and the start scale 1 are not consecutive scales

# 1,2,2,1,,3,1,2 -> is valid bacause all number seems to be consetive , sum up to 12 and the last and start are consecutive.
# Can it more optimized?

mp = {
    1  : [2,3],
    2 : [1, 2],
    3 : [1]
}
res =[]
target = 12
def backtrack(cur  , cur_sum , cur_list, start):
    #base case
    if cur  + cur_sum == target and cur     in mp[start]:
        res.append(cur_list + [cur])
        
        return
    
    if cur + cur_sum > target:
        return         
    
    vals = mp[cur]
    
    for v in vals:
        backtrack(v , cur+cur_sum , cur_list+[cur], start)
        
for i in range(1 , 4):
    backtrack(i, 0 , [] , i)
    
print(res)
