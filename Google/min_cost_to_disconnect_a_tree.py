# Python code to find the minimum weight required to disconnect all leaf nodes in a tree.

def min_disconnect_cost(u, parent_weight, tree):
    """
    Computes the minimal total cost to disconnect all leaf nodes in the subtree rooted at node u.
    
    Parameters:
    - u: current node
    - parent_weight: weight of the edge connecting u to its parent
    - tree: dictionary representing the tree
    
    Returns:
    - Minimum total weight required to disconnect all leaf nodes in the subtree rooted at u
    """
    if u not in tree or len(tree[u]) == 0:
        # Leaf node: return the weight of the edge to its parent
        return parent_weight
    else:
        # Option 1: Cut the edge to the parent
        cost_cut_edge = parent_weight

        # Option 2: Do not cut the edge to the parent, sum over children
        cost_no_cut = 0
        for v, weight_uv in tree[u]:
            cost_no_cut += min_disconnect_cost(v, weight_uv, tree)

        # Return the minimum of the two options
        return min(cost_cut_edge, cost_no_cut)

# Example 1
# Tree structure:
# A has children B and C
# B has children D and E
# Edges with weights: A-B:2, A-C:4, B-D:2, B-E:1
tree1 = {
    'A': [('B', 2)],
    'B': [('C', 3)],
    'C': [("D" , 1)]
    # 'C', 'D', 'E' are leaf nodes
}

# Start recursion from root 'A' with parent_weight set to infinity (since root has no parent)
min_cost1 = min_disconnect_cost('A', float('inf'), tree1)
print("Minimum total weight required (Example 1):", min_cost1)  # Output: 6

# Example 2
# Tree structure:
# A has children B and C
# B has children D and E
# Edges with weights: A-B:3, A-C:4, B-D:1, B-E:1
tree2 = {
    'A': [('B', 3), ('C', 4)],
    'B': [('D', 1), ('E', 1)],
    # 'C', 'D', 'E' are leaf nodes
}

min_cost2 = min_disconnect_cost('A', float('inf'), tree2)
print("Minimum total weight required (Example 2):", min_cost2)  # Output: 6
