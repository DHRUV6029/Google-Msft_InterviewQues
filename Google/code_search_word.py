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


board= [['Q','E', 'P', 'L', 'E'],
        ['W', 'N', 'M', 'I', 'N']]


word = "PEN"

word = list(word)
jump = 2

direc = []

def generate_jump_space_dfs(max_jump):
    jump_space = set()
    st = [(0,0,max_jump)]
    while st:
        i ,j , jump_left = st.pop()
        
        if jump_left:
            
            for dr , dc in [(0,1),(0,-1),(-1,0),(1,0)]:
                nr= dr+i
                nc = dc+j 
                
                jump_space.add((nr ,nc))
                st.append((nr, nc, jump_left-1))
                
    jump_space.remove((0,0))
    return jump_space
                
        
direc = generate_jump_space_dfs(jump)
        
def backtrach(r ,c , word, board):
    if len(word) == 0:
        return True
    
    if r < 0 or c < 0 or r > len(board)-1 or c > len(board[0])-1 or board[r][c]!= word[0]:
        return False
    
    board[r][c] = "*"
    
    flag = False
    
    for dr , dc in direc:
        nr , nc  = dr+r ,dc + c
        
        flag = backtrach(nr, nc , word[1:] , board)
        
        if flag:
            return True
        
    board[r][c] = word[0]
    
            


flag =1
for i in range(0 ,len(board)):
    for j in range(0,len(board[0])):
        if backtrach(i ,j , word, board):
            print(True)
            flag=0
            break
    
if flag == 1:        
    print(False)
                
            
            
    
    
    