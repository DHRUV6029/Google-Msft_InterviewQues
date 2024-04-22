# Below is a coding problem I was asked during a Google technical phone screen:

# Question: Convert an array of email folder objects to an array of Gmail label strings.

# // Sample input:

# folders = [
#     {id: 27, parentId: 15, name: 'projects'},
#     {id: 81, parentId: 27, name: 'novel'},
#     {id: 15, parentId: 0, name: 'personal'}, // a parentId of 0 means root
#     {id: 35, parentId: 27, name: 'blog'},
# ]

# // Sample output:

# labels = [
#     'personal/projects',
#     'personal/projects/novel',
#     'personal',
#     'personal/projects/blog',
# ]

import collections
folders = [
    {'id': 27, 'parentId': 15, 'name': 'projects'},
    {'id': 81, 'parentId': 27, 'name': 'novel'},
     {'id': 15, 'parentId': 0, 'name': 'personal'},
     {'id': 35, 'parentId': 27, 'name': 'blog'},
]


id_name = collections.defaultdict(int)
parent_chd = collections.defaultdict(list)

for folder in folders:
    id_name[folder['id']] = folder['name']
    
root = None
for folder in folders:
    if id_name[folder['parentId']] !=0:
        parent_chd[id_name[folder['parentId']]].append(folder['name'])
    else:
        root = folder['name']
        
def printAllLabesl(root, path):
    #assuing its a tree structure with not cycels
    #so not keepping visited 
    
    
    path.append('/'+root)
    
    print(''.join(path)[1:])
    
    for neigh in parent_chd[root]:
        printAllLabesl(neigh , path)
        
    path.pop()
    
    
printAllLabesl(root, [])
        
    
    