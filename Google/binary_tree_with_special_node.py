# Timeline : July (2nd Week)
# Reschedule count : 3
# Total Time spent : 38-40 mints

# Pre Join : This is my very first interview with any non-indian interviewer, Technically I was scared if I could understand the accent and mindset of the interviewer as I had no experience with foreign interviewers (Typical low key insecurities).

# Join : Interviewer came after 7 minutes. Called me on my mobile first, Then we came up with GMeet link. Senior engineer from a very important google product

# Started : So, It started. He seemed a very cool guy. No shit talk, directly moved into the problem.

# The problem :
# There is a binary tree (a sample tree was made with “/”, “\” ). Tree has total three kind of nodes.

# Normal nodes : with two children
# Leaf nodes : no children
# Special nodes : only one children.
# Multiple consecutive Special nodes make a Special nodes Chain. like (a → b → c) are the node chain, so length is 3 here. First, he said to find the max chain length, later changed it to return all the unique chain lengths and its count in the tree.

# I discussed about the approach and complexities, went for DFS. And answer will be returned in a dictionary (Hashmap)

# Seems so easy problem but while implementing I messed up a little. Anyway while dry running I found my issue and fixed it. Throughout the process I explained everything and shared my thought process. He seemed very pleased with the solution.
# (Time spent so far 20+ mints)

# Then, he came up with the follow up, Proposed a huge tree similar to this, And made it open for all teams to use. How I am going to optimize it.
# First of all, I didn’t understand the requirements, I questioned multiple times and tried to extract any hints, But to understand his hints I needed some hints too. Any way I proposed something different, I told to zip the special nodes chain and make a list of it. But The solution he was expecting, I couldn’t come up with. Anyway he liked mine (The zipping solution)

# End discussion :
# I have always been a good, light hearted discusser. We discussed few google topics. He ensured me here, Nobody came up with the follow-up solution and that’s not going to affect my flow (consolidation I presumed)

# Results :
# Recruiter called me after 5 days. Feedback was good. She planned next 4 rounds in upcoming weeks.

# All the posts are coming in order, stay tuned, Will share links


import collections
mp = collections.defaultdict(int)


class TreeNode:
    def __init__(self , val = 0 ,left =None , right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    
    def count_speacial_chains(self, root , chain_len):
        
        if not root.left and not root.right:  #we are at leaf node no need to explore further
            return
        
        if root.left and root.right:
            self.count_speacial_chains(root.left , 0)
            self.count_speacial_chains(root.right , 0)
        elif root.left and not root.right:
            self.count_speacial_chains(root.left , chain_len+1)
            mp[chain_len+1]+=1
        elif root.right and not root.left:
            self.count_speacial_chains(root.right, chain_len+1)
            mp[chain_len+1]+=1


        return
    
t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(3)

s = Solution()
s.count_speacial_chains(t ,0)
print("vfrve")


        
            
            

          


        
