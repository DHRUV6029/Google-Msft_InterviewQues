# 3
# Anonymous User
# Anonymous User
# Last Edit: March 15, 2024 7:19 AM

# 623 VIEWS

# Hi ,

# I gave my first Technical Phone Screening round on 6th March 2024,
# Can't reveal the exact questions,

# Question is about a frog which can go left or right with with maximum possible step be l for left and r for right, i.e. frog can move right 0 or 1, or 2 or ... r times, given start and destination, find minimum steps to reach.
# Something related to making maximum number using digits(1 to 9) where using a digit has some associated cost(can be different for dif digits), and we have fixed money we can use.
# But I don't know why my recruiter is taking too long to respond. Not even replying ? Is it normal, it's my first time giving Interview out of college,
# Exp: 8 Months in SWE

cost = [1, 2, 3, 4, 5, 6, 7, 8, 9]
budget = 15


memo = {}

def dp(remain_budget , remain_digits):
    if remain_budget == 0  or not remain_digits:
        return 0
    
    if (remain_budget , tuple(remain_digits)) in memo:
        return memo[(remain_budget , tuple(remain_digits)) ]
    
    ans=0
    
    for d in remain_digits:
        if remain_budget - cost[d-1]<0:
            continue
        
        ans = max(ans ,  dp(remain_budget - cost[d-1] , [digit for digit in remain_digits if d != digit])
                  * 10 + d)
        
    memo[(remain_budget , tuple(remain_digits))] = ans
    return ans


print(dp(budget , list(range(1, 10))))
