# ; Given a 2D keyboard, and a “maximum jump distance” jump_distance, determine if a given word can be constructed using the characters in the keyboard, obeying the jump_distance. A jump can be up, down, right, or left. But NO diagonal, i.e. a diagonal jump would naturally consume 2 units of jump distance.

# ; Arbitrary keyboard given as list of lists, e.g.:

# ; [[‘Q’,’ X’, ‘P’, ‘L’, ‘E’],
# ;  [‘W’, ‘A’, ‘C’, ‘I’, ’N’]]
# ; Jumping distance given as an integer, e.g. 2.

# ; “PENCIL”, jump_distance = 2

# ; P → E → N → C → I → L True

# ; “PACE”, jump_distance = 2

# ; P → A → C → can’t go to E! False

# ; implement a method word_can_be_typed(keyboard, word, jump_distance) that returns True if the word can be constructed, else False.
import collections


board= [['Q','X', 'P', 'L', 'E'],
        ['W', 'A', 'C', 'I', 'N']]


type_word = "PENCIL"



#Question depends on a very minute detials if duplicates are allowed or not
#Case-1 If duplicates are allowed than need to backtrack
#Case-2 Are duplicates not allowed than (Hashmap and manhattan distance works)

#We will write assuming Duplicates are allowed

row = len(board)
col = len(board)
word = "PENCIL"
def backtrack(r , c ,board , word , jump_left):
    if len(word) == 0:
        return
    
    if r<0 or r==row or c < 0  or c == col or board[r][c]!= word[0]:
            return False
        
    flag = False
    board[r][c] = "#"   #mark as visited
    
    if jump_left > 0:
        for dr , dc in [(0,1),(1,0),(0,-1),(-1,0)]:
            nr = r+dr
            nc = c+dc
            flag = backtrack(nr , nc , board , word[1:] , jump_left-1)

            if flag:
                return True
            
        board[r][c] = word[0]
                    
        

for x in range(0 , row):
    for y in range(0 , col):
        if backtrack(x , y, board , word , 2):
            print(True)
            

        print(False)
        
    
        


