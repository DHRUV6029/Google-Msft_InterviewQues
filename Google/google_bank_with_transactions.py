# Consider a bank with some intial amount of money. Consider an array which represents list of transactions which are going to come through customers. + means deposit - means withdrawl. Bank can choose from which customer they want to start serving the customers and they can refuse any number of customers. But once they start they have to serve till the time its impossible to serve the customers. Maximize the total customers bank can serve.

# Example :
# Bank has 1 unit of money intially.
# Customer transactions : [1, -3, 5, -2, 1]

# answer = 3

# Bank starts with customer with deposit of 5
# 1+ 5 = 6
# 6 - 2 = 4
# 4 + 1 =5

# If bank starts at in index 0 can only serve 1 customer
# 1+1 =2
# 2-3 = -1 not possible


transactions  = [1,2,-9,3,4,4]

ans =0

l =0
b = 1
s = b
for r in range(0,len(transactions)):
    #if transaction is positice
    s+=transactions[r]
    
    if s < 0:
        ans = max(ans , r-l)
        l = r
        while l < len(transactions) and  b + transactions[l]<0:
            l+=1
        if l  > r:
            r =l
        s = b
        
    r+=1
ans = max(ans, r-l)   
print(ans)
            
    

