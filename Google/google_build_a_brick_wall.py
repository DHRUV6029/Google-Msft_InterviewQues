# 2184. Number of Ways to Build Sturdy Brick Wall
# Medium
# Topics
# Companies
# Hint
# You are given integers height and width which specify the dimensions of a brick wall you are building. You are also given a 0-indexed array of unique integers bricks, where the ith brick has a height of 1 and a width of bricks[i]. You have an infinite supply of each type of brick and bricks may not be rotated.

# Each row in the wall must be exactly width units long. For the wall to be sturdy, adjacent rows in the wall should not join bricks at the same location, except at the ends of the wall.

# Return the number of ways to build a sturdy wall. Since the answer may be very large, return it modulo 109 + 7.

 

height = 2
width = 3
bricks = [1,2]

#bricks represrnt the w 
#1 Approach (represent a single row config as a mask)
def generate_single_row_mask(w , width , masks, bricks, cur_mask):
    if w == width:
        masks.append(cur_mask)
        
    if w:
        cur_mask = cur_mask | (1 << (w-1))  #(setting the bit that represents the crack)
    for b in bricks:
        if w+b <= width:
            generate_single_row_mask(w+b, width , masks , bricks , cur_mask)
                
    return masks


#memo 
#when performing dfs (at each h, we need the ans , and also which mask we used)

memo = {}
def stack_bricks(h , cur , masks):
    if h == 0:
        return 1 #we finished one path of the DFS tree
    
    if (h, cur) in memo:
        return memo[(h, cur)]  #return pre computer result
    
    ans = 0
    for mask in masks:
        if mask & cur == 0:  #condition of strudyness
            ans = ans + stack_bricks(h-1, mask , masks)
            ans = ans % (10**9+7)
            
    memo[(h, cur)] = ans
    return ans


masks = generate_single_row_mask(0, width , [] , bricks, 0)
ans = stack_bricks(height  , 0 , masks)

print(ans)