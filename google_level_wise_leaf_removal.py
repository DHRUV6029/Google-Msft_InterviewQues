# For a rooted tree with any arbitary number of children for each node,
# not necessarily n-ary tree.
# Remove all the leaf nodes, and store them in a list, this would create
# new leaf nodes. Repeat untill all the nodes are removed
# Conditions : Freshly created leaf nodes(node whose children are removed)
# should not be removed just after its children are removed, unless
# there's no other option for us, then we can remove it


import collections

mp =collections.