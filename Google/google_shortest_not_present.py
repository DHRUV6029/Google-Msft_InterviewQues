# Given a array of bytes (c++ string or char array or unit_8 array).

# Please find a shortest byte sequence that does not present in the input array.

# assume that "byte" contains only "a" to "f"
# input: "abcdefacbeddefd"

# "a" is present
# "b" is present
# ..
# "f" is present
# "aa" is not present
# "ab" is present
# "ac" is present

# you can return "aa" or "ad" or "ae"... "ff"
# but not "ab" "ac" "bc"

# testcases
# input - aabcdf
# output - e
# Check for single byte shortest byte sequence a,b,c, .... f

# input - abcdefacbeddefd
# output - aa
# check for aa, ab, ac, .... ff

# input - abcdefacbeddefdaabbccddeeff
# output - ab

# input contains arbitrary bytes ('\x00' to '\xff'), not only letters
# small testcase: input length <= 16MB
# large testcase: input length <= 4GB

# you have 8GB ram

# How to solve this proble


# #we need to fnind a subseqauemce that is not present
# #so 
# eg "abbccac"  ---> "cb"     for simplicity bytes are a b c

# #Intuition - 1   if string till ith index has a chars >= k (k is ni of bytes)


alpha = 'abcdefghijklmnopqrstuvwxyz'

s = 'abbccac'  
k = 6 #'abcdef'
n = k + 1

ans = ''
hset = set()
    
for i in range(0,len(s)):
    hset.add(s[i])
    if len(hset) == k:
        hset.clear()
        ans+=s[i]
            
for i in alpha:
    if i not in hset:
        ans+=i
        break
        
print(ans)

            
            
            



