
# This one works for Strings
def RabinKarp(l): #l represent cuirrent substring length
            mod = 10**9+7
            h = 0
            a = 26
    
            mp =  collections.defaultdict(list)
    
    
            for i in range(0, l):
                h = (h*a+nums[i])%mod
        
            mp[h].append(0)
            al = pow(a, l , mod)
            for i in range(1 , len(s)-l+1):
                #compute the rolling hash in constant time
                h = (h*a - nums[i-1]*al + nums[i+l-1]) % mod
        
                if h in mp:
                    cur = nums[i:i+l]
                    #one more check to avoid collision in hashing #this hashing will collide for certian patterns
                    for idx in mp[h]:
                        if nums[idx:idx+l] == cur:
                            return i
                
                mp[h].append(i)
        
            return -1



#But there's a practical issue — more collisions. With a large base and single mod, different subarrays are more likely to collide. The brute-force collision check (nums[idx:idx+l] == cur) handles correctness, but if many collisions happen, it slows things down.
#Fix: use double hashing to reduce collisions:

def rabin_karp(l):
    mod1 = 10**9 + 7
    mod2 = 10**9 + 9  # second mod
    a1 = 100003       # first base (prime > max value)
    a2 = 100019       # second base (different prime)

    h1 = h2 = 0
    mp = collections.defaultdict(list)

    for i in range(l):
        h1 = (h1 * a1 + nums[i]) % mod1
        h2 = (h2 * a2 + nums[i]) % mod2
    mp[(h1, h2)].append(0)

    al1 = pow(a1, l, mod1)
    al2 = pow(a2, l, mod2)

    for i in range(1, n - l + 1):
        h1 = (h1 * a1 - nums[i-1] * al1 + nums[i+l-1]) % mod1
        h2 = (h2 * a2 - nums[i-1] * al2 + nums[i+l-1]) % mod2
        key = (h1, h2)
        if key in mp:
            cur = nums[i:i+l]
            for idx in mp[key]:
                if nums[idx:idx+l] == cur:
                    return i
        mp[key].append(i)
    return -1
