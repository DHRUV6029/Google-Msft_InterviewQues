# <!-- LeetCode 1820. Maximum Number of Accepted Invitations
#Hungarian Algorithm
# There are m boys and n girls in a class attending an upcoming party.

# You are given an m x n integer matrix grid, where grid[i][j] equals 0 or 1. If grid[i][j] == 1, then that means the ith boy can invite the jth girl to the party. A boy can invite at most one girl, and a girl can accept at most one invitation from a boy.

# Return the maximum possible number of accepted invitations.

# Example 1:

# Input: grid = [[1,1,1],
#               [1,0,1],
#               [0,0,1]]
# Output: 3

#   Explanation: The invitations are sent as follows:
#   - The 1st boy invites the 2nd girl.
#   - The 2nd boy invites the 1st girl.
#   - The 3rd boy invites the 3rd girl.
# Example 2:

# Input: grid = [[1,0,1,0],
#               [1,0,0,0],
#               [0,0,1,0],
#               [1,1,1,0]]
# Output: 3

# Explanation: The invitations are sent as follows:
# -The 1st boy invites the 3rd girl.
# -The 2nd boy invites the 1st girl.
# -The 3rd boy invites no one.
# -The 4th boy invites the 2nd girl.
# Constraints:

# grid.length == 

# grid[i].length == n

# 1 <= m, n <= 200

# grid[i][j] is either 0 or 1. -->


grid = [[1,0,1,0],
        [1,0,0,0],
        [0,0,1,0],
        [1,1,1,0]]

m = len(grid)  #----> boys
n = len(grid[0]) #----> girls


matches = {} #----> girls -----> boy (pair)

def maximize_accepted_invitations(boy , visit):
    
    for girl in range(n):
        #do not ask if already asked girl have some self respect, or do not ask grils way out of your league
        if girl in visit or grid[boy][girl]==0:
            continue
        
        visit.add(girl)
        #if a girl is not matched or a matched girls ,boy can find some other girl
        
        if girl not in matches or maximize_accepted_invitations(matches[girl], visit):
            matches[girl] = boy
            return True
        
    return False

ans = 0

for boy in range(n):
    ans+=maximize_accepted_invitations(boy ,set())
    
print(ans)
    


        
        