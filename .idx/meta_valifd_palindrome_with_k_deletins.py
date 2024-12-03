
# Space: O(k) for recursion stack
s = "aabbbbbcjdksca"
k = 7
l , r  = 0 ,len(s)-1
def valid_palindrome_with_k_deletions(l , r, s, n):
    while l < r:
        if s[l] != s[r]:

            if n == 0:
                return False
            
            return valid_palindrome_with_k_deletions(l+1, r, s, n-1) or \
            valid_palindrome_with_k_deletions(l, r-1,s,n-1)
        
        else:
            l+=1
            r-=1

    return True

print(valid_palindrome_with_k_deletions(0,len(s)-1 , s, k))    

#######Memoization#########################

memo = {}

#state will be  l,r, k

def solve(l, r,s , k):
    #base case
    if l >= r:
        return True
    
    if (l,r,k) in memo:
        return memo[(l,r,k)]
    
    if s[l]!=s[r]:
        if k > 0:
            memo[(l,r,k)] = solve(l+1,r,s,k-1) or solve(l, r-1,s,k-1)
            return memo[(l,r,k)]
        return False
    
    memo[(l,r,k)] = solve(l+1, r-1, s, k)

    return memo[(l,r,k)]

print(solve(0,len(s)-1 , s, k))
