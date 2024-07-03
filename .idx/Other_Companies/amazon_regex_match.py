regex = "..()*e*"
patterns = []


def check_inner_match(s , t):
    x , y = 0 , 0 

    while x < len(s) and y < len(t):
        if s[x]==t[y] or t[y] == '.':
            x+=1
            y+=1
        else:
            return False
    return x >= len(s) and y >= len(t)

def check_match(regex, pattern):
    i = 0
    j = 0

    while i < len(regex) and j < len(pattern):
        #handles ()* cases
        if regex[i] == "(":
            k = regex[i:].index("*") + i

            inner_pattern = regex[i+1 : k-1]
            
            
            while j < len(pattern) and inner_pattern != '' and check_inner_match(pattern[j:j+len(inner_pattern)] , inner_pattern):
                j+=len(inner_pattern)
            i = k+1
        elif i+1 < len(regex) and regex[i].isalpha() and regex[i+1] == "*":
            inner_pattern = regex[i]
            if pattern[j] != inner_pattern:
                return False
            while j <len(pattern) and pattern[j] == inner_pattern:
                j+=1
            i+=2
        elif regex[i] == '.' or regex[i] == pattern[j]:  #handles . and a == a cases
            i+=1
            j+=1
        else:
            return False
        
    return i >= len(regex) and j >= len(pattern)

print(check_match(regex , "abeee"))
