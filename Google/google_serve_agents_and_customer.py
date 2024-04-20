# Calculate the total wait time for a customer C to speak to an agent given N agents, M customers, and T[] time for an agent to serve a customer. T[i] represents the amount of time it takes for an agent i to serve one customer. One agent can serve one customer at a time. All N agents can serve concurrently. The customer chooses the agent with the lowest wait time.

# Examples:

# N = 2
# M = 2
# T = [4, 5]
# First customer chooses agent 1. Second customer chooses agent 2.
# Customer C will wait 4 minutes.
# N = 2
# M = 4
# T = [4, 5]
# First customer chooses agent 1. Second customer chooses agent 2.
# Third customer chooses agent 1. Forth customer chooses agent 2.
# Customer C will wait 8 minutes.
# Initial questions:

# Bounds on N and M - No bounds
# Can N or M be zero - Both can be zero
# Are the T values constant - Yes
# Are the T values integers - Yes


import heapq
N = 2
M =4   
T = [5 , 4]

org = len(T)

# Cth customer is M+1 customer
heapq.heapify(T)


cur_time = 0
for i in range(0 ,M-org):
    val = heapq.heappop(T)
    heapq.heappush(T,2*val)
    
print(T[0])
        
    