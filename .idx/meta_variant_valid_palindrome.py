import collections
s = "abc"

def solution(s):

    def isvalid(i):
        return s[i].isalpha()
    

    
    def check(i ,j):
        while i < j:
            while i < j and not isvalid(i):
                i+=1
            while i < j and not isvalid(j):
                j-=1
            if s[i] != s[j]:
                return False
            
            i+=1
            j-=1
        return True
    
    i = 0 
    j = len(s)-1

    while i < j:
        while i < j and not isvalid(i):
            i+=1
        while i < j and not isvalid(j):
            j-=1

        if s[i] != s[j]:
            return check(i+1, j) or check(i ,j-1)
        
        i+=1
        j-=1
    return True

s = solution("!!!!!baa")
print(s)

    
