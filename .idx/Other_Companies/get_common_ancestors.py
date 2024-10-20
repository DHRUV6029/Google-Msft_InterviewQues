def get_common_ancestors(data, n1, n2):
    parent_dict = defaultdict(list)
    for parent, child in data:
        parent_dict[child].append(parent)

    def get_ancestors(node):
        ancestors = set()
        stack = [node]
        while stack:
            curr = stack.pop()
            parents = parent_dict[curr]
            for parent in parents:
                ancestors.add(parent)
                stack.append(parent)
        return ancestors

    n1_parents = get_ancestors(n1)
    n2_parents = get_ancestors(n2)
    output = []
    for n in n1_parents:
        if n in n2_parents:
            output.append(n)
    return output
