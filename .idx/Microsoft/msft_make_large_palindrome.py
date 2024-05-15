# Recently I have given a codility test in Microsoft.
# There was 2 questions for 80 minutes. And both the code was running and all test cases passed. Still Recruiter told me its not cleared. Seems they were looking for the score which is not to the mark.
# Anyone know based on what they are giving score and what are they expecting.

# Question 1:
# You are given a string S, which consists entirely of decimal digits (0−9).
# Using digits from S, create a palindromic number with the largest possible decimal value.
# You should use at least one digit and you can reorder the digits.

# A palindromic number remains the same when its digits are reversed; for instance, "7", "44" or "83238".
# Any palindromic number you create should not, however, have any leading zeros, such as in "0990" or "010".
# For example, decimal palindromic numbers that can be created from "8199" are:
# "1", "8", "9", "99", "919" and "989".

# Among them, “989” has the largest value.

import collections
S = "54321"

mp = collections.defaultdict(int)
ans = ''
for i in S:
    mp[int(i)]+=1
    
#approach All evens coiunts can be utlilized for odd 1 can be at centre and , 
# others around it

nums = []

mp = dict(sorted(mp.items() , key=lambda x : x[0], reverse=True))

middle =[]
#place all evens only build half of the palindrome we will build the other has
for k , v in mp.items():
    if v % 2 == 0:
        nums.extend([k]*(v//2))
    else:
        nums.extend([k]*((v-1)//2))
        middle.append(k)
        
#now nedd to process odd nums but here is the thing odds 
middle.sort(reverse=True)

left = ''.join(str(i) for i in nums)

right = left[::-1]


if middle:
    ans = left + str(middle[0]) + right
else:
    ans = left  + right
    
ans = ans.strip('0')

print(ans if ans else '0')
    





