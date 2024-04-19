# I got a mail from recuiter if I am interested in open positions because I took google foobar. They gave me enough time to prepare and when I was comfortable I took the call for interview.

# I was interviewed on 8th Jan and the interviewer asked me these two questions.

# Imagine an array class with only 3 operations GetAt(), SetAt() and SetAll(). Implement all the methods as O(1).
# Given denominations D and a max value MAX, find the smallest set of coins that can exactly construct any value 1 <= n <= MAX.
# **The explanation goes like this.
# D is a vector, sorted increasing, which describes the monetary system; e.g. {1, 5, 10, 25} for a U.S. penny, nickel, dime, quarter.
# MAX is in the same units as D.
# The output should be a vector of the same order as D, where each coefficient is how many of that coin you have. "Smallest set" refers to the total number of coins in the set. Some inputs may have multiple equally good answers; you may choose any such answer.

# The wasn't able to solve any of those. I provided solutions but they were not up to the mark.
# The first one is pretty easy.

# Edit:
# For the second question I came up with a approach which i would like to share:


D = [1,5,10,25]


need = 0
MAX =100
cur_cover = 0
coins = []
i = 0
while True:
    #check if next is smaller than eqaul to cur_need
    
        
    if i+1 < len(D) and need >= D[i+1]:
        i+=1
    
    cur_cover = cur_cover + D[i]

    need = cur_cover+1
    coins.append(D[i])
    if cur_cover >= MAX:
        print(coins)
        break
    
    
print(coins)
    
    
import collections 
class Array:
    def __init__(self) -> None:
        self.hset = collections.defaultdict(int)
        self.time_stmap = 0
        self.setAll = None
        
    def getAt(self, i):
        self.time_stmap+=1
        if i in self.hset:
            val  , _ts  = self.hset[i]
            
            if self.setAll:
                if _ts < self.setAll[1]:
                    return self.setAll[0]
        
            return val
        
        return None
    
    def setAt(self, i , val):
        self.time_stmap+=1
        
        self.hset[i] = [val ,self.time_stmap]
        
        
    def setAllVals(self, val):
        self.time_stmap+=1
        self.setAll = [val , self.time_stmap]
        
        
a = Array()


a.setAt(0, 1)
a.setAt(3, 6)

print(a.getAt(0))

a.setAllVals(1999)

print(a.getAt(0))




        
