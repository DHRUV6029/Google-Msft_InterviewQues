# """
# Google Phone Screen

# inequalities=[ ("a","<","b"),("b",">","c"),("a","<","c"),("d",">","b")]
# Given a list of inequalities does it hold true/false?
# o/p=
# [ ("a","<","b"),("b","<","a") ] False
# [ ("d",">","a")] True
# """

# I used a dict of lists to keep track of left and right elements. Interviewer was expecting a ***** (I dont want to bias the solution) I'll addi it at the end. Unsure about this!!

# UPDATED
import collections
inequalities=[ ("a","<","b"),("b",">","c"),("a","<","c"),("d",">","b")]  #assuming these are corredt and valid

a = [ ("a","<","b"),("b","<","a") ]
b =[ ("d",">","a")] 

#Approach 
#Assuming therr are only two pairs, we can easliy extend the for loo]
# > ---- directed edge

mp = collections.defaultdict(list)
for a , s , b in inequalities:
    if s == '<':
        mp[a].append(b)
    else:
        mp[b].append(a)
        
def dfs(src , dest):
    #no need of visit
    if src == dest:
        return True
    
    for neigh in mp[src]:
        return dfs(neigh , dest)
    
    
    return False
def solution(vals):
    for v in vals:
       
        
        src , s, dest  = v[0] ,v[1] ,v[2]
        if s == '>':
            src = b
            dest = a
                
        if not dfs(src, dest):
            return False
            
    return True



print(solution([ ["a","<","b"],["b","<","a"]]))
print(solution( [[ "d",">","a"]]))
                
        
        
        