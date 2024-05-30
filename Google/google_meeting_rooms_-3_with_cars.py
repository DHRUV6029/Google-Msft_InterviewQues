# Position : L4
# Experience : 3 Years
# Round : Phone Screening
# Problem 1 :Given one struct of time interval with using that i have to return in bool that are they overlapping 2 intervals or not.
# struct TimeInterval{
# int id ;
# int startTime;
# int endTime;
# };
# bool overlapping( TimeInterva t1, TimeInterva t2){}
# this problem i completed in 8-10 minutes with dryrun of the test cases;
# Problem 2 : Given stream of time interval tell that min how many cars will be used to book for all timeintervals;
# Given : {{1,3}, {2,5},{6,8},{7,10},{9,10}}
# output :
# car1 : {1,3},{6,8},{9,10}
# car2 : {2,5},{7,10}
# taken 2-3 minutes for building the logic in my mind
# I explained the algorithm : 5-7 minutes
# written the psuedocode : 5 minutes
# completed 80% of the code : 10 minutes
# Explained Time complexity and Space Complexity : 2-3 minutes
# and Times up

import heapq
import collections
intervals =  [[0,10],[1,5],[2,7],[3,4]]

#Assumption intervals are streaming in sorted order with start and end time
free_cars = [i for i in range(1 , len(intervals)+1)]


intervals.sort()
cars = []
mp = collections.defaultdict(list)
for s, e in intervals:
    #non overlapping intervals try to see if previously used car is avalubale 
    while cars and cars[0][0] <= s:
        time, car_id = heapq.heappop(cars)
        heapq.heappush(free_cars , car_id)
    
    if free_cars:
        car_id = heapq.heappop(free_cars)
        heapq.heappush(cars , [e, car_id])
    else:
        time , car_id = heapq.heappop(cars)
        heapq.heappush(cars , (e+time-s , car_id))

    mp[car_id].append((s, e))

print(mp)
    



             
