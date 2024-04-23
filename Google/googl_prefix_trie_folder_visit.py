# oday 19 Dec 2023, from 01:00 to 01:45 PM, I have a Google Phone Screen Interview

# History
# Since I am looking for a change I am facing lots of DSA rounds in interviews, and I failed in all
# Hence I decided to learn DSA and then Apply,
# Surprisingly I got a call from Google HR to explore an opportunity,
# I was not prepared, but I wanted interview experience, Hence I proceeded unprepared :(,

# Programming Language Used: Kotlin

# Question
# I felt easy/Medium Level questions during the interview

# Q. Given a list of all files and folders, and list of selected files and folder
# send selected compressed files or folder as input to CLI(Command Line Interface)
# by the following condition

# If all files under the folder are selected, then only select that folder, CLI auto-selects all files under that folder
# If any file is not selected under that folder then get its path to output
# Same for subfolders and files
# File and folder name could be any size, not compulsory single char file and folder name
# File and Folder separated by '/' character
# Samples, Input


all_files = [
"a/b.txt",
"b/c.txt",
"b/d.txt",
"c/e.txt",
"c/f/a.txt",
"c/f/b.txt",
"c/g.txt",
"d/a/b.txt",
]

selected_Files = [
"b/c.txt",
"b/d.txt",
"c/f",
"d/a/b.txt",
]



#Step -1 Build a Trie
class TrieNode:
    def __init__(self) -> None:
        self.child = {}
        self.is_File = False
        self.child_count = 0
        self.visit_count = 0
        
        
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        
    def buildTrie(self, folder_path):
        cur = self.root
        folders  = folder_path.split("/")
        
        for val in folders:
            
            if val not in cur.child:
                cur.child[val] = TrieNode()
                
            cur.child_count+=1
            cur = cur.child[val]
            
        cur.is_File = True
    
    def markTrie(self , path):
        cur = self.root
        folders = path.split("/")
        
        for val in folders:
            if val in cur.child:
                cur.visit_count+=1
            cur = cur.child[val]
            
        cur.visit_count+=1
        
        
       
       
 
t = Trie()

for file in all_files:
    t.buildTrie(file)
    
for file in selected_Files:
    t.markTrie(file)
    
res = []  
def dfs(node, path):
    if node.visit_count == 0:
        return 
    
    if node.visit_count == node.child_count or (node.visit_count==1 and 
                                                node.is_File):
        res.append(path[1:])
        
    else:
        for child in node.child:
            dfs(node.child[child], path + "/" + child)
            
dfs(t.root , "")

print(res)
        
