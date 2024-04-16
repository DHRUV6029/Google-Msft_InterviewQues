# Today 19 Dec 2023, from 01:00 to 01:45 PM, I have a Google Phone Screen Interview

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
# val all_files = [
# "a/b.txt",
# "b/c.txt",
# "b/d.txt",
# "c/e.txt",
# "c/f/a.txt",
# "c/f/b.txt"
# "c/g.txt",
# "d/a/b.txt",
# ]

# val selected_Files = [
# "b/c.txt",
# "b/d.txt",
# "c/e.txt",
# "c/f/a.txt",
# "c/f/b.txt",
# "d/a/b.txt",
# ]

# Output: [
# "b", <-- both files under folder 'b' is selected hence choose folder itself
# "c/e.txt", <-- file 'e' selected but 'g' is not, hence choose a single file
# "c/f" <-- all files under folder 'f' is selected hence chosen folder 'f'
# "d" <-- all files and folders selected under 'd' folder
# ]


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.child_count = 0
        self.visit = 0
        self.isFile = False
        
        
class Trie():
	def __init__(self):
		self.root = TrieNode()

	def insert(self, path):
		curr = self.root
		for name in path.split("/"):
			if not name in curr.children:
				curr.children[name] = TrieNode()
			curr.children_count += 1
			curr = curr.children[name]
		curr.is_file = True

	def mark(self, path):
		curr = self.root
		for name in path.split("/"):
			if name in curr.children:
				curr.visited_count += 1
			curr = curr.children[name]
		curr.visited_count += 1
  
  
class Solution:
    t = TrieNode()
    
    #build the trie
    #visit the trie
    res = []
    
    def dfs(node, current_path):
        if node.visit == 0:
            return
        
        elif node.visit == node.children or node.visit == 1 and node.isFile:
            res.append(current_path[1:])
        else:
            for child in node.children:
                dfs(child , "/"+child)
                
                

