# YOE: 2.8
# Position: SDE 2
# Location: Noida
# Date: March 2024

# Telephonic Round:
# I had a phone interview with Google recently. In the Telephonic round initilly she explained me how the interview evaluation happens at Google.
# The she asked me about the map workiing and searching TIme complexity in Map(Avg and worst). She was satisfied with my answer and the round 1 was scheduled after 2 weeks.

# Round1 :

# A Binary tree was given where its nodes represents as the employee and every parent node as the manager of its child node. i had to design an algorithm to determine if a manager's salary is higher than the sum of their employees' salaries or not Then answer i hve to give as a boolean.
# I discussed the algorithm approach with the interviewer he was satisfied with my approach. First i had wrotten the psuedo code then i written the actual code.
# I was rejected due to i had solved only one problem but in actually there are always 2 problems asked by the interviwer in Google's interview. The time was over so he didnt asked me the next Question.


class Tree:
    def __init__(self, val,left =None , right = None) -> None:
        self.val = val
        self.left = left
        self.right = self.right

res =[0, True] 
def is_mnanager_salary_higher_than_all(node):  #node represent the manager
    if not node:
        return [0 , True]
    
    #exlpore employees on left
    l = is_mnanager_salary_higher_than_all(node.left)
    
    #we will do early prunning if on this bracnh we founf the cur sum of employers salary
    #higer than stop do not go to right
    if l[1]==False:
        return [0, False]
    
    r =  l = is_mnanager_salary_higher_than_all(node.right)
    
    if l[1]==False:
        return [0, False]
    
    return [node.val + l[0] + l[0] , node.val + l[0] + l[0] <= node.val]



######buildinf a tree

t = Tree(4000)
    