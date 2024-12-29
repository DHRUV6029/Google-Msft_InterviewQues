
# Example 1:

# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true
# Explanation: The word "internationalization" can be 
# abbreviated as "i12iz4n" ("i nternational iz atio n").
# Example 2:]

# Input: word = "apple", abbr = "a2e"
# Output: false
#"hello", "h*llo"  __, True
# Explanation: The word "apple" cannot be abbreviated as "a2e".

# Also pattern could have * which could match 0 or more characters

import re


word = "internationalization"
abbr = "i*123"

memo = {}
def is_all_star(abbr, j):
    for i in range(j ,len(abbr)):
        if abbr[i]!='*':
            return False
    
    return True

def is_Number(val):
    return val.isdigit()


def isMatch(i , j , memo):
    #base case
    if (i , j) in memo:
        return memo[(i, j)]
    
    if j >= len(abbr):
        return i >= len(word)
    
    if i >= len(word):
        return is_all_star(abbr, j)
    

    if abbr[j] == '*':
        memo[(i,j)] = isMatch(i+1,j,memo) or isMatch(i, j+1,memo)
        return memo[(i,j)]
    
    if is_Number(abbr[j]):
        num = 0
            
            
        while j < len(abbr) and is_Number(abbr[j]):
            if num == 0 and  abbr[j] == '0':
                return False
            num = num * 10+int(abbr[j])
            j+=1

        if i + num > len(word):
            return False
            
        return isMatch(i+num , j ,memo)
    
    if word[i] != abbr[j]:
        return False
    
    return isMatch(i+1 ,j+1,memo)  #for eqaul cases


print(isMatch(0 ,0, {}))  # True

# word = "abc"
# abbr = "*bc"

# Tree visualization:
#                     (0,0)
#                 /          \
#            (1,0)          (0,1)  [match 'a' with * OR skip *]
#           /     \            |
#       (2,0)    (1,1)       (1,1)  [same state!]
#       /   \       |          |
#   (3,0) (2,1)   (2,2)     (2,2)  [same state!]
