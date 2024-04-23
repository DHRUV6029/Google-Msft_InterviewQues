# You work as a consultant and have clients in cityA and cityB. On a given day,
# say i, you can either
# work in cityA and make Ai dollars or you can work in cityB and make Bi dollars. You can also spend
# the day traveling between cityA and cityB in which case your earnings that day are 0.
# Given Al,A2, ....An and B1, B2,....., Bn, return a schedule S of N days which maximizes your earnings,
# where S is a string of length N, and Si = A/B/T where A means work in cityA, B means work in cityB
# T means travel on day i. You can start either in cityA or cityB. Example1: A = [23, 4,5 ,101] B = [21,1,10, 100] The optimal schedule S here would be ->"ATBB"
# Example 2:
# A[25,10,15,10,70] B = [5,5,50,5,30] The optimal schedule S here would be-> "ATBTA"

A= [25,10,15,10,70]
B =[5,5,50,5,30]

memo = {}
def citySwitch(city):
    if city == 'A':
        return 'B'
    
    if city == 'B':
        return 'A'

def getMaxRoute(i , cur_city):
    if i >= len(A):
        return 0 ,''
    
    #if already computed 
    if (i , cur_city) in memo:
        return memo[(i , cur_city)]
    
    profit_1 , route_1 = getMaxRoute(i+1, cur_city)  #staying at same city
    profit_2 , route_2 = getMaxRoute(i+2 , citySwitch(cur_city)) #we are switching the city so missing profit on i+1 th day
    
    
    #decide where to go
    if profit_1 >= profit_2:
        cur_profit = profit_1 + (A[i] if cur_city == 'A' else B[i])
        cur_route =  cur_city + route_1
    else:
        cur_profit = profit_2 + (B[i] if cur_city == 'B' else A[i])
        cur_route = cur_city + 'T' + route_2
        
    memo[(i , cur_city)] = [cur_profit , cur_route]
    
    return memo[(i , cur_city)]

start_a = getMaxRoute(0, 'A')
start_b = getMaxRoute(0 , 'B')


print(max(start_a , start_b , key=lambda x : x[0]))


def switch(current):
    return 'B' if current == 'A' else 'A'

