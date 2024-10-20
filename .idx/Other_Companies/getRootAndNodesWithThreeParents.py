def getRootAndNodesWithThreeParents(arrayOfRelationships):
    parent_dict = defaultdict(list)
    all_nodes = set()
    for parent, child in arrayOfRelationships:
        parent_dict[child].append(parent)
        all_nodes.add(child)
        all_nodes.add(parent)

    no_parents = []
    three_parents = []
    for node in all_nodes:
        if node not in parent_dict:
            no_parents.append(node)
        elif len(parent_dict[node]) == 3:
            three_parents.append(node)
    return [no_parents, three_parents]

print getRootAndNodesWithThreeParents(parent_child_pairs)
