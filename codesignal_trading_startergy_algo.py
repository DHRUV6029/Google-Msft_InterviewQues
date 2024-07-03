nums = [2,4,1,5,2,6,7]
s =    [0,1,0,-1,1,-1,0]
k = 2
ans = 0


def make_0(cur_sum , cur_c , i):
    if cur_c == -1:
        cur_sum+=nums[i]
    elif cur_c == 1:
        cur_sum-=nums[i]

    return cur_sum


def make_1(cur_sum , cur_c , i):
    if cur_c == 0:
        cur_sum+=nums[i]
    elif cur_c ==-1:
        cur_sum+=(2*nums[i])
    return cur_sum

def make_minus_1(cur_sum , cur_c , i):
    if cur_c == 0:
        cur_sum-=(nums[i])
    elif cur_c == 1:
        cur_sum-=(2*nums[i])

    return cur_sum
    



def calcualteProfit():
    profit = 0
    for i in range(0,len(nums)):
        profit = profit +  s[i]*nums[i]
    return profit

def slide_window():
    global ans
    cur = calcualteProfit()
    ans = max(ans , cur)

    for i in range(0,k):
        if i < k//2:
            cur = make_0(cur , s[i] , i)
        else:
            cur = make_1(cur , s[i] , i)

    ans = max(ans, cur)

    l = 0
    fl = k//2

    for r in range(k,len(nums)):
        cur = make_1(cur , s[r] , r)  #adding to the end
        cur = make_0(cur , 1 , fl) #setting the middle one
        
        if s[l] == 0:
            cur = make_0(cur , 0  , l)
        elif s[l] == 1:
            cur = make_1(cur , 0  , l)
        else:
            cur = make_minus_1(cur , 0  , l)

        l+=1
        fl+=1


        ans = max(cur , ans)

    return ans

ans = slide_window()
print(ans)
