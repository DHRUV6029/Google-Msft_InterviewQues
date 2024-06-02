class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        mp = collections.defaultdict(list)
        #for less 
        if n < 2:
            return [0]

        for u , v in edges:
            mp[u].append(v)
            mp[v].append(u)


        leaves = []

        for k , v in mp.items():
            if len(v) == 1:
                leaves.append(k)


        total_nodes= n

        while total_nodes > 2:
            total_nodes-=len(leaves)
            new_leaves = []


            while leaves:
                cur = leaves.pop()

                #remove it from the 
                next_leaf = mp[cur].pop()

                #remove the edfes
                mp[next_leaf].remove(cur)

                if len(mp[next_leaf]) ==1:
                    #this is the next leaf
                    new_leaves.append(next_leaf)

            leaves = new_leaves

        return(leaves)

        
