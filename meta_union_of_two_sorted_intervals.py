#union of two intervals 

first = [[1,3], [3,6]]
second = [[2,4], [8,7]]


res = []
def union(arr1 , arr2):
    cur_start , cur_end = -1 ,-1
    i ,j = 0 , 0
    while i < len(first) or j < len(second):
        if j == len(second) or (i < len(first)) and first[i][0] <= second[j][0]:
            start , end =  first[i]
            i+=1
        else:
            start , end = second[j]
            j+=1


        if cur_end < start:  #no overlap
            if cur_end != -1:
                res.append([cur_start , cur_end])
        
            cur_start = start
            cur_end = end
        else:
            cur_end = max(cur_end , end)


    if cur_end != -1:
        res.append([cur_start, cur_end])


ans = union(first , second)
print(res)



