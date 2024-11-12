import collections
Tree = [1, 2, 3, 4, 5, None, None]
n = 5
Edges =  [[1, 2], [2, 4]] 


mp = collections.defaultdict(set)
seen = set()
ans = []
i  =0
while i < len(Tree):
    if Tree[i] is None:
        i+=1
        continue

    if ((2 * i)+ 1) < len(Tree) and Tree[(2 * i) + 1] is not None:
        mp[Tree[i]].add(Tree[2 * i + 1])
    else:
        mp[Tree[i]] = set()


    if ((2*i) + 2) < len(Tree) and Tree[(2 * i) + 2] is not None:
        mp[Tree[i]].add(Tree[(2 * i) + 2])
    else:
        mp[Tree[i]] = set()

    i+=1


for u , v in Edges:
    mp[u].remove(v)


def visit_components(node):
    count=1
    seen.add(node)

    for neigh in mp[node]:
        if neigh not in seen:
            count+=visit_components(neigh)
    return count



for i in range(1 , n+1):
    if i not in seen:
        a  =visit_components(i)
        ans.append(a)

print(ans)



